/* editeur-python.js — l'éditeur Python intégré aux pages du dépôt (Pascal, 04/11/2026).
 *
 * POURQUOI
 * --------
 * « Dans cette séquence on demande d'aller sur l'interface Vittascience et l'interface n'est pas jointe à
 * l'exercice. » Vittascience refuse d'être affiché dans une autre page : l'éditeur vient donc dans la page,
 * comme le mode code de Vittascience — la zone de code, ▶ Exécuter, la console. Vittascience reste un lien
 * facultatif, écrit dans le HTML du bloc.
 *
 * LE BLOC HTML, POSÉ DANS CHAQUE EXERCICE (il marche aussi sans JavaScript : la zone et le lien)
 * -------------------------------------------------------------------------------------------------
 *   <div class="editeur-py" id="vs1" data-fichier="3e-VARIABLES-TON NOM" [data-simulation="id"]>
 *     <label for="py_a3">…</label>
 *     <textarea id="py_a3" class="editeur-py-code" rows="6" wrap="off" spellcheck="false">CODE DE DÉPART</textarea>
 *     <p class="editeur-py-vitta">… <a class="btn vs-lien" href="https://fr.vittascience.com/python/?mode=code…">Vittascience, si tu préfères</a></p>
 *     <p class="editeur-py-sansjs">…ce qu'on fait sans JavaScript…</p>
 *   </div>
 *   <script src="../../../../_ressources-communes/editeur-python/editeur-python.js" defer></script>
 *
 * Le code de départ est le contenu écrit du <textarea> (sa valeur par défaut). Le programme de l'élève est la
 * VALEUR du <textarea> : la page le sauvegarde avec ses autres champs (même identifiant), le composant lui
 * envoie un « change » à chaque frappe (après une courte pause) et suit la restauration de la page.
 * `data-simulation` nomme un <script type="text/x-python"> de la page : des fonctions simulées (capteur,
 * pompe…), exécutées AVANT le programme de l'élève, sans décaler ses numéros de ligne.
 *
 * LE MOTEUR : Skulpt 1.2.0 (licence MIT : skulpt/LICENSE.txt ; provenance et raisons : LISEZMOI.md), déposé à côté de ce fichier, chargé au
 * PREMIER ▶ Exécuter seulement. Aucune requête réseau : les deux fichiers sont lus par chemin relatif.
 *
 * CE QUE LA PAGE PEUT EN FAIRE
 *   window.EditeurPython.executer(code, {simulation, entrees, limiteActive, limiteTotale}) → Promise<{sortie, erreur, arret}>
 *     exécute sans rien afficher (une vérification qui juge en exécutant ; 3 s de calcul, 10 s en tout, par défaut) ;
 *   window.EditeurPython.instance(idDuChamp) → {executer(), arreter(), code, sortie()} ;
 *   l'événement « editeur-py:fin » (bulle depuis le bloc) après chaque exécution :
 *     detail = {bloc, champ, code, sortie, erreur, arret}.
 */
(function () {
  "use strict";
  if (window.EditeurPython) return;

  var SCRIPT = document.currentScript;
  var BASE = (function () {
    try { return new URL(".", SCRIPT && SCRIPT.src ? SCRIPT.src : location.href).href; }
    catch (e) { return ""; }
  })();

  var LIMITE_ACTIVE = 5000;    // ms de calcul sans pause : au-delà, c'est une boucle sans fin
  var LIMITE_TOTALE = 60000;   // ms au total (attentes comprises, hors input()) : un while True qui attend
  var LIGNES_MAX = 1000;       // lignes de console au plus

  /* ───────────────────────── chargement de Skulpt, au premier ▶ ───────────────────────── */
  var chargement = null;
  function chargerScript(nom) {
    return new Promise(function (ok, ko) {
      var s = document.createElement("script");
      s.src = BASE + "skulpt/" + nom;
      s.onload = function () { ok(); };
      s.onerror = function () { ko(new Error("chargement impossible : " + nom)); };
      document.head.appendChild(s);
    });
  }
  function chargerSkulpt() {
    if (window.Sk && window.Sk.builtinFiles) return Promise.resolve();
    if (!chargement) {
      chargement = chargerScript("skulpt.min.js").then(function () { return chargerScript("skulpt-stdlib.js"); });
      chargement.catch(function () { chargement = null; });
    }
    return chargement;
  }

  /* ───────────────────────── une exécution à la fois (Skulpt est global) ───────────────────────── */
  var file = Promise.resolve();
  function enFile(f) { var p = file.then(f, f); file = p.then(function () {}, function () {}); return p; }

  var ARRET = { arret: "bouton" }, TROP_LONG = { arret: "total" }, DEBORDE = { arret: "lignes" };

  /* Exécute `code` (après `prelude`). o.ecrire(texte), o.lire(invite) → Promise<texte>, o.signal.arret. */
  function moteur(code, prelude, o) {
    return enFile(function () {
      return chargerSkulpt().then(function () {
        var Sk = window.Sk;
        var decalage = prelude ? prelude.split("\n").length : 0;
        var source = prelude ? prelude + "\n" + code : code;
        var lignes = 0, deborde = false, sortie = "";
        var debut = Date.now(), attenteEntree = 0;
        var signal = o.signal || {};
        var limiteTotale = o.limiteTotale || LIMITE_TOTALE;
        Sk.configure({
          output: function (t) {
            if (deborde) return;
            var n = (t.match(/\n/g) || []).length;
            if (lignes + n > LIGNES_MAX) { deborde = true; return; }
            lignes += n; sortie += t; if (o.ecrire) o.ecrire(t);
          },
          read: function (f) {
            if (Sk.builtinFiles && Sk.builtinFiles.files[f] !== undefined) return Sk.builtinFiles.files[f];
            throw "File not found: '" + f + "'";
          },
          __future__: Sk.python3,
          inputfunTakesPrompt: true,
          inputfun: function (invite) {
            var t0 = Date.now();
            return Promise.resolve(o.lire ? o.lire(String(invite == null ? "" : invite)) : "").then(function (v) {
              attenteEntree += Date.now() - t0; return v;
            }, function (e) { attenteEntree += Date.now() - t0; throw e; });
          },
          execLimit: o.limiteActive || LIMITE_ACTIVE, yieldLimit: 100, killableWhile: true, killableFor: true
        });
        function verifier() {
          if (signal.arret) throw ARRET;
          if (deborde) throw DEBORDE;
          if (Date.now() - debut - attenteEntree > limiteTotale) throw TROP_LONG;
        }
        Sk.execStart = Date.now();
        return Sk.misceval.asyncToPromise(function () {
          return Sk.importMainWithBody("<stdin>", false, source, true);
        }, {
          "Sk.promise": function (r) {
            verifier();
            var t0 = Date.now();
            return new Promise(function (ok, ko) {
              var annule = false;
              signal.interrompre = function () { annule = true; ko(ARRET); };
              r.data.promise.then(function (x) {
                if (annule) return;
                signal.interrompre = null;
                Sk.execStart += Date.now() - t0;
                try { verifier(); r.data.result = x; ok(r.resume()); } catch (e) { ko(e); }
              }, function (e) {
                if (annule) return;
                signal.interrompre = null;
                if (e === ARRET) { ko(ARRET); return; }
                Sk.execStart += Date.now() - t0;
                try { r.data.error = e; ok(r.resume()); } catch (e2) { ko(e2); }
              });
            });
          },
          "*": function () { verifier(); }
        }).then(function () {
          return { sortie: sortie, erreur: null, arret: deborde ? "lignes" : null };
        }, function (e) {
          if (e && e.arret) return { sortie: sortie, erreur: null, arret: e.arret };
          return { sortie: sortie, erreur: decrire(e, code, decalage), arret: null };
        });
      });
    });
  }

  /* ───────────────────────── les erreurs, expliquées en français ───────────────────────── */
  function nomType(e) {
    if (e && e.tp$name) return e.tp$name;
    if (e && e.constructor && e.constructor.tp$name) return e.constructor.tp$name;
    return "Erreur";
  }
  function messageBrut(e) {
    try { if (e && e.args && e.args.v && e.args.v.length) return String(e.args.v[0].v !== undefined ? e.args.v[0].v : e.args.v[0]); }
    catch (x) {}
    return String(e && e.message || e || "");
  }
  /* Les messages de Skulpt, ramenés à ceux de Python 3 quand ils diffèrent. */
  function commePython3(type, m) {
    var c = /^cannot concatenate '(\w+)' and '(\w+)' objects$/.exec(m);
    if (c && c[1] === "str") return 'can only concatenate str (not "' + c[2] + '") to str';
    if (c) return "unsupported operand type(s) for +: '" + c[1] + "' and '" + c[2] + "'";
    if (/^integer division or modulo by zero$/.test(m)) return "division by zero";
    if (type === "TimeLimitError") return "le programme tournait encore après " + LIMITE_ACTIVE / 1000 + " s";
    if (type === "SyntaxError" && /^bad (input|token)/.test(m)) return "invalid syntax";
    if (/^EOF in multi-line statement$/.test(m)) return "'(' was never closed";
    return m;
  }
  function sansCommentaire(l) {
    var dans = null, i;
    for (i = 0; i < l.length; i++) {
      var ch = l[i];
      if (dans) { if (ch === dans) dans = null; }
      else if (ch === '"' || ch === "'") dans = ch;
      else if (ch === "#") return l.slice(0, i);
    }
    return l;
  }
  function hors_chaines(l) { return sansCommentaire(l).replace(/"[^"]*"|'[^']*'/g, '""'); }
  function retrait(l) { var m = /^[ \t]*/.exec(l); return m[0].replace(/\t/g, "    ").length; }
  var BLOC = /^\s*(if|elif|else|while|for|def|try|except|finally|with|class)\b/;

  function diagnosticSyntaxe(lignes, n, m) {
    var l = lignes[n - 1] || "", nette = hors_chaines(l).trimEnd();
    var k = n - 2; while (k >= 0 && !hors_chaines(lignes[k]).trim()) k--;
    var prec = k >= 0 ? hors_chaines(lignes[k]).trimEnd() : "";
    var nPrec = k + 1;
    if (/___|▢/.test(l)) return { ligne: n, texte: "Il reste un trou à compléter ligne " + n + " : remplace « ___ » par ce qui manque." };
    if (/unindent does not match/.test(m))
      return { ligne: n, texte: "Le décalage de la ligne " + n + " ne correspond à aucun bloc : une ligne d'un bloc se décale exactement comme les autres lignes de ce bloc (4 espaces par niveau)." };
    if (/'return' outside function/.test(m))
      return { ligne: n, texte: "« return » ne s'écrit que DANS une fonction : sous une ligne « def …: », décalé de 4 espaces." };
    if (/[À-ÿ]/.test(nette.replace(/""/g, "")) && /bad token|bad input/.test(m))
      return { ligne: n, texte: "Ligne " + n + ", un nom contient une lettre accentuée. Cet éditeur, comme les cartes programmables, n'en veut pas dans les noms : écris « humidite », pas « humidité ». Les accents restent permis entre guillemets." };
    // les guillemets de la ligne
    var sc = sansCommentaire(l), nd = (sc.match(/"/g) || []).length, ns = (sc.replace(/"[^"]*"/g, "").match(/'/g) || []).length;
    if (nd % 2 === 1 || ns % 2 === 1)
      return { ligne: n, texte: "Ligne " + n + ", un guillemet est ouvert et jamais refermé : un texte commence ET finit par un guillemet, « \"comme ceci\" »." };
    // les parenthèses : la première ligne où une parenthèse reste ouverte
    var prof = 0, ouverte = 0, i, j;
    for (i = 0; i < lignes.length; i++) {
      var t = hors_chaines(lignes[i]);
      for (j = 0; j < t.length; j++) {
        if ("([{".indexOf(t[j]) >= 0) { if (prof === 0) ouverte = i + 1; prof++; }
        else if (")]}".indexOf(t[j]) >= 0) { prof--; if (prof < 0) return { ligne: i + 1, texte: "Ligne " + (i + 1) + ", une parenthèse est fermée sans avoir été ouverte : compte-les, il en faut autant de « ( » que de « ) »." }; }
      }
      if (prof > 0 && i + 1 >= n && /EOF/.test(m)) break;
    }
    if (prof > 0 || /EOF in multi-line/.test(m))
      return { ligne: ouverte || n, texte: "Ligne " + (ouverte || n) + ", une parenthèse est ouverte et jamais refermée : il en faut autant de « ( » que de « ) »." };
    if (/^\s*(if|elif|while)\b/.test(nette) && /[^=!<>]=[^=]/.test(nette.replace(/^\s*(if|elif|while)/, " ")))
      return { ligne: n, texte: "Ligne " + n + ", dans un test, on compare avec « == » (deux signes égal). Un seul « = » RANGE une valeur dans une variable : il n'a rien à faire après « if »." };
    if (BLOC.test(nette) && !/:\s*$/.test(nette))
      return { ligne: n, texte: "Ligne " + n + ", il manque les deux-points « : » à la fin. Après if, elif, else, while, for et def, la ligne finit toujours par « : »." };
    if (prec && /:\s*$/.test(prec) && retrait(l) <= retrait(lignes[k]))
      return { ligne: n, texte: "Ligne " + n + ", il manque le décalage. La ligne " + nPrec + " finit par « : » : les lignes de son bloc se décalent de 4 espaces (touche Tab)." };
    if (prec && !/:\s*$/.test(prec) && retrait(l) > retrait(lignes[k]))
      return { ligne: n, texte: "Ligne " + n + ", la ligne est décalée alors que rien ne l'exige : la ligne " + nPrec + " ne finit pas par « : ». Enlève les espaces au début de la ligne " + n + "." };
    if (k < 0 && retrait(l) > 0)
      return { ligne: n, texte: "Ligne " + n + ", la première ligne du programme ne doit pas être décalée : enlève les espaces au début." };
    if (prec && BLOC.test(prec) && !/:\s*$/.test(prec))
      return { ligne: nPrec, texte: "Ligne " + nPrec + ", il manque les deux-points « : » à la fin. Après if, elif, else, while, for et def, la ligne finit toujours par « : »." };
    return { ligne: n, texte: "Python ne comprend pas l'écriture de la ligne " + n + ". Relis-la signe par signe : les deux-points, les parenthèses, les guillemets, le décalage." };
  }

  function nomsDu(code) {
    var noms = {}, re = /\b([A-Za-z_][A-Za-z0-9_]*)\s*(?:=(?!=)|\()/g, m;
    while ((m = re.exec(code))) noms[m[1]] = 1;
    (code.match(/\bdef\s+([A-Za-z_]\w*)/g) || []).forEach(function (d) { noms[d.replace(/def\s+/, "")] = 1; });
    return Object.keys(noms).concat(["print", "input", "int", "float", "str", "range", "len", "round", "True", "False", "None", "type", "abs", "bool"]);
  }

  function decrire(e, code, decalage) {
    var type = nomType(e), brut = messageBrut(e), m = commePython3(type, brut);
    var tb = (e && e.traceback) || [];
    var ligne = null, dansSimulation = false, i;
    for (i = 0; i < tb.length; i++) {
      if (tb[i] && tb[i].lineno) {
        if (tb[i].lineno > decalage) { ligne = tb[i].lineno - decalage; break; }
        dansSimulation = true;
      }
    }
    if (ligne === null && tb.length && tb[0].lineno && !dansSimulation) ligne = tb[0].lineno - decalage;
    var lignes = code.split("\n"), texte = "", titre = "";
    if (type === "SyntaxError" || type === "IndentationError" || type === "TabError") {
      var d = diagnosticSyntaxe(lignes, Math.max(1, Math.min(ligne || 1, lignes.length + 1)), brut);
      ligne = d.ligne; texte = d.texte;
      titre = /décal/.test(texte) ? "Erreur de décalage (indentation)" : "Erreur d'écriture (syntaxe)";
    } else if (type === "NameError") {
      var nom = (/name '([^']+)'/.exec(brut) || [])[1] || "?";
      var connus = nomsDu(code), proche = null;
      connus.forEach(function (c) { if (!proche && c !== nom && c.toLowerCase() === nom.toLowerCase()) proche = c; });
      titre = "Nom inconnu";
      texte = "Ligne " + ligne + ", Python ne connaît pas « " + nom + " ». " +
        (proche ? "Tu voulais sans doute écrire « " + proche + " » : les majuscules comptent. "
                : "Vérifie l'orthographe, majuscules comprises (Print n'est pas print) ; et une variable doit recevoir une valeur (" + nom + " = …) AVANT la ligne qui l'utilise. ") +
        (/^[A-Za-zÀ-ÿ]+$/.test(nom) && !proche ? "Si c'est un texte, il lui faut des guillemets : \"" + nom + "\"." : "");
    } else if (type === "TypeError") {
      var op = /for ([+\-*\/%]|\*\*|\/\/): '(\w+)' and '(\w+)'/.exec(m), conc = /concatenate str \(not "(\w+)"\)/.exec(m) || /^cannot concatenate '(\w+)' and '(\w+)'/.exec(brut);
      var cmp = /'([<>=!]+)' not supported between instances of '(\w+)' and '(\w+)'/.exec(m);
      var args = /(\w+)\(\) takes (\d+) positional arguments? but (\d+) (?:was|were) given/.exec(m);
      titre = "Erreur de type";
      if (conc || (op && op[1] === "+" && (op[2] === "str" || op[3] === "str"))) {
        texte = "Ligne " + ligne + ", le « + » mélange un texte (str) et un nombre. Entre deux textes, + COLLE ; entre deux nombres, + ADDITIONNE ; entre les deux, Python refuse de deviner. " +
          "Pour calculer : transforme le texte en nombre avec int(…) ; pour afficher : transforme le nombre en texte avec str(…), ou sépare-les par une virgule dans print.";
      } else if (op && (op[2] === "str" || op[3] === "str")) {
        texte = "Ligne " + ligne + ", « " + op[1] + " » entre un texte (str) et un nombre : on ne soustrait pas, on ne multiplie pas, on ne divise pas un texte. Ta variable contient sans doute des chiffres ENTRE GUILLEMETS : enlève-les, ou transforme le texte avec int(…).";
      } else if (cmp) {
        texte = "Ligne " + ligne + ", tu compares un texte et un nombre. Souvent, la valeur vient de input(), qui renvoie TOUJOURS un texte : écris int(input(…)) pour obtenir un nombre.";
      } else if (args) {
        texte = "Ligne " + ligne + ", la fonction « " + args[1] + " » attend " + args[2] + " valeur(s) entre ses parenthèses, et tu lui en donnes " + args[3] + ".";
      } else if (/not callable/.test(m)) {
        texte = "Ligne " + ligne + ", des parenthèses suivent un nom qui n'est pas une fonction (une variable, un nombre ?). Vérifie que tu n'as pas donné à une variable le nom d'une fonction.";
      } else {
        texte = "Ligne " + ligne + ", l'opération ne va pas avec le type des valeurs (nombre entier int, nombre à virgule float, texte str…). Affiche-les avec print(type(…)) pour voir leur type.";
      }
    } else if (type === "ValueError") {
      var val = (/: '(.*)'$/.exec(brut) || [])[1];
      titre = "Valeur impossible";
      texte = /invalid literal for int/.test(brut)
        ? "Ligne " + ligne + ", int() ne sait pas faire un nombre entier avec « " + (val === undefined ? "?" : val) + " » : le texte ne doit contenir que des chiffres (et un signe −). Pour un nombre à virgule, c'est float(…), avec un POINT : 2.5."
        : "Ligne " + ligne + ", la valeur donnée ne convient pas à l'opération.";
    } else if (type === "ZeroDivisionError") {
      titre = "Division par zéro"; texte = "Ligne " + ligne + ", tu divises par zéro : c'est impossible, même pour un ordinateur. Regarde quelle variable vaut 0 à ce moment-là.";
    } else if (type === "IndexError") {
      titre = "Case inexistante"; texte = "Ligne " + ligne + ", tu demandes une case de la liste qui n'existe pas. Une liste de 3 éléments a les cases 0, 1 et 2.";
    } else if (type === "TimeLimitError") {
      titre = "Boucle sans fin ?";
      texte = "Ton programme calculait encore après " + LIMITE_ACTIVE / 1000 + " secondes sans s'arrêter : la page l'a arrêté" + (ligne ? " (il tournait vers la ligne " + ligne + ")" : "") + ". Une boucle while dont la condition ne devient jamais fausse ? Vérifie qu'une ligne DANS la boucle fait changer la variable testée.";
    } else {
      titre = "Erreur à l'exécution";
      texte = (ligne ? "Ligne " + ligne + ", " : "") + "Python s'est arrêté. Lis le message ci-dessous et regarde cette ligne de près.";
    }
    if (dansSimulation && ligne === null) texte += " (L'erreur s'est produite dans une fonction simulée de la page : vérifie ce que tu lui donnes entre parenthèses.)";
    return { type: type, ligne: ligne, message: type + ": " + m, titre: titre, explication: texte };
  }

  /* ───────────────────────── l'API sans écran ───────────────────────── */
  function prelude(simulation) {
    if (!simulation) return "";
    if (/\n|\(/.test(simulation)) return simulation;
    var s = document.getElementById(simulation);
    return s ? s.textContent.replace(/^\s*\n/, "").replace(/\s+$/, "") : "";
  }
  function executer(code, o) {
    o = o || {};
    var entrees = (o.entrees || []).slice();
    return moteur(String(code), prelude(o.simulation), {
      lire: function () { return Promise.resolve(entrees.length ? String(entrees.shift()) : ""); },
      signal: {}, limiteActive: o.limiteActive || 3000, limiteTotale: o.limiteTotale || 10000
    });
  }

  /* ───────────────────────── le composant ───────────────────────── */
  var instances = {};
  function el(tag, cls, texte) { var e = document.createElement(tag); if (cls) e.className = cls; if (texte != null) e.textContent = texte; return e; }
  function bouton(cls, texte, titre) { var b = el("button", "btn editeur-py-btn " + cls, texte); b.type = "button"; if (titre) b.title = titre; return b; }
  function propreNom(n) { return (n || "mon-programme").replace(/\.py$/i, "").replace(/[\\\/:*?"<>|]+/g, "-").trim() || "mon-programme"; }

  function monter(bloc) {
    var ta = bloc.querySelector("textarea.editeur-py-code");
    if (!ta || bloc.classList.contains("editeur-py--actif")) return;
    bloc.classList.add("editeur-py--actif");
    var id = ta.id || ("py_" + Math.random().toString(36).slice(2, 8));
    ta.id = id;
    var depart = ta.defaultValue.replace(/^\n/, "");
    var fichierDefaut = bloc.getAttribute("data-fichier") || "mon-programme";
    ta.setAttribute("wrap", "off"); ta.setAttribute("spellcheck", "false");
    ta.setAttribute("autocapitalize", "off"); ta.setAttribute("autocomplete", "off");
    ta.setAttribute("autocorrect", "off"); ta.setAttribute("data-gramm", "false");
    if (!ta.getAttribute("aria-describedby")) ta.setAttribute("aria-describedby", id + "_aide");

    // ── la barre du fichier : nom, ⬇, 📂
    var barreF = el("div", "editeur-py-fichier");
    var labNom = el("label", "editeur-py-nom-lab", "📄 Nom du fichier"); labNom.htmlFor = id + "_nom";
    var nom = el("input", "editeur-py-nom"); nom.type = "text"; nom.id = id + "_nom"; nom.value = fichierDefaut;
    nom.setAttribute("spellcheck", "false"); nom.setAttribute("autocomplete", "off");
    var ext = el("span", "editeur-py-ext", ".py");
    var groupeNom = el("span", "editeur-py-nom-groupe"); groupeNom.appendChild(nom); groupeNom.appendChild(ext);
    var bTel = bouton("editeur-py-telecharger", "⬇ Télécharger mon .py");
    var bOuv = bouton("editeur-py-ouvrir", "📂 Ouvrir mon .py");
    var choix = el("input", "editeur-py-choix"); choix.type = "file"; choix.accept = ".py,.txt,text/x-python,text/plain";
    choix.setAttribute("aria-label", "Choisir ton fichier .py à ouvrir dans l'éditeur"); choix.tabIndex = -1; choix.hidden = true;
    barreF.appendChild(labNom); barreF.appendChild(groupeNom); barreF.appendChild(bTel); barreF.appendChild(bOuv); barreF.appendChild(choix);

    // ── la zone : marge numérotée + textarea
    var zone = el("div", "editeur-py-zone");
    var marge = el("div", "editeur-py-marge"); marge.setAttribute("aria-hidden", "true");
    var interieur = el("div", "editeur-py-marge-int"); marge.appendChild(interieur);
    ta.parentNode.insertBefore(barreF, ta);
    ta.parentNode.insertBefore(zone, ta);
    zone.appendChild(marge); zone.appendChild(ta);
    var aide = el("p", "editeur-py-aide", "⌨ Tab = 4 espaces · pour quitter la zone au clavier : Échap, puis Tab · ton programme est gardé tout seul dans cette page.");
    aide.id = id + "_aide";

    // ── la barre d'exécution
    var barreX = el("div", "editeur-py-barre");
    var bExe = bouton("editeur-py-executer", "▶ Exécuter");
    var bStop = bouton("editeur-py-arreter", "⏹ Arrêter"); bStop.disabled = true;
    var bDep = bouton("editeur-py-depart", "↺ Remettre le code de départ");
    barreX.appendChild(bExe); barreX.appendChild(bStop); barreX.appendChild(bDep);
    var etat = el("p", "editeur-py-etat"); etat.setAttribute("role", "status");

    // ── la console
    var titreC = el("p", "editeur-py-console-titre", "🖥 Console — ce que ton programme affiche");
    titreC.id = id + "_console_titre";
    var cons = el("div", "editeur-py-console"); cons.setAttribute("role", "log"); cons.setAttribute("aria-live", "polite");
    cons.setAttribute("aria-labelledby", titreC.id); cons.tabIndex = 0;
    var vide = el("span", "editeur-py-vide", "(rien pour l'instant : clique ▶ Exécuter)"); cons.appendChild(vide);

    // ── l'impression : le programme écrit et la dernière sortie (ou des lignes vides)
    var imp = el("div", "editeur-py-imp");
    var impCode = el("pre", "editeur-py-imp-code"), impSortie = el("pre", "editeur-py-imp-sortie");
    imp.appendChild(el("p", "editeur-py-imp-titre", "Mon programme (fichier " + fichierDefaut + ".py) :"));
    imp.appendChild(impCode);
    imp.appendChild(el("p", "editeur-py-imp-titre", "Ce que la console a affiché :"));
    imp.appendChild(impSortie);

    var apres = zone.nextSibling;
    [aide, barreX, etat, titreC, cons, imp].forEach(function (n) { bloc.insertBefore(n, apres); });

    // ── la valeur du champ : suivre la restauration de la page (qui écrit .value)
    var proto = Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype, "value");
    try {
      Object.defineProperty(ta, "value", {
        configurable: true,
        get: function () { return proto.get.call(ta); },
        set: function (v) { proto.set.call(ta, v); majVue(); }
      });
    } catch (x) {}

    var derniereSortie = "", enCours = null, ligneErreur = null, minuterie = null;

    function majVue() {
      var n = Math.max(1, ta.value.split("\n").length), t = "", i;
      for (i = 1; i <= n; i++) t += (i > 1 ? "\n" : "") + i;
      interieur.textContent = t;
      if (ligneErreur) marquer(ligneErreur);
      ta.rows = Math.min(18, Math.max(5, n + 1));
      interieur.style.transform = "translateY(" + (-ta.scrollTop) + "px)";
      impCode.textContent = ta.value.trim() ? ta.value : "\n\n\n\n\n";
      impCode.classList.toggle("editeur-py-imp-vide", !ta.value.trim());
    }
    function marquer(n) {
      ligneErreur = n;
      var lignes = interieur.textContent.split("\n");
      interieur.innerHTML = "";
      lignes.forEach(function (l, k) {
        var s = el("span", (k + 1) === n ? "editeur-py-ko" : "", l);
        interieur.appendChild(s); if (k < lignes.length - 1) interieur.appendChild(document.createTextNode("\n"));
      });
    }
    function demarquer() { if (ligneErreur) { ligneErreur = null; majVue(); } }
    function sauver() { ta.dispatchEvent(new Event("change", { bubbles: true })); }
    function bientotSauver() { clearTimeout(minuterie); minuterie = setTimeout(sauver, 500); }

    ta.addEventListener("input", function () { demarquer(); majVue(); bientotSauver(); });
    ta.addEventListener("scroll", function () { interieur.style.transform = "translateY(" + (-ta.scrollTop) + "px)"; });
    ta.addEventListener("blur", function () { clearTimeout(minuterie); });

    // ── le clavier : Tab = 4 espaces, Maj+Tab retire, Entrée garde le décalage, Échap libère Tab
    var libre = false;
    function remplacer(debut, fin, texte, selDebut, selFin) {
      ta.focus();
      ta.setSelectionRange(debut, fin);
      var ok = false;
      try { ok = document.execCommand && document.execCommand("insertText", false, texte); } catch (x) { ok = false; }
      if (!ok) { ta.setRangeText(texte, debut, fin, "end"); ta.dispatchEvent(new Event("input", { bubbles: true })); }
      if (selDebut != null) ta.setSelectionRange(selDebut, selFin);
    }
    ta.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { libre = true; etat.textContent = "⌨ Tab te fait maintenant sortir de la zone."; return; }
      if (e.key === "Tab" && !libre && !e.ctrlKey && !e.altKey && !e.metaKey) {
        e.preventDefault();
        var v = ta.value, a = ta.selectionStart, b = ta.selectionEnd;
        var dl = v.lastIndexOf("\n", a - 1) + 1;
        if (a === b && !e.shiftKey) { remplacer(a, b, "    "); return; }
        var fl = v.indexOf("\n", b - (b > a && v[b - 1] === "\n" ? 1 : 0)); if (fl < 0) fl = v.length;
        var bloc = v.slice(dl, fl), nouveau;
        if (e.shiftKey) nouveau = bloc.split("\n").map(function (l) { return l.replace(/^( {1,4}|\t)/, ""); }).join("\n");
        else nouveau = bloc.split("\n").map(function (l) { return "    " + l; }).join("\n");
        remplacer(dl, fl, nouveau, dl, dl + nouveau.length);
        return;
      }
      if (e.key === "Tab") { libre = false; return; }
      libre = false;
      if (e.key === "Enter" && !e.shiftKey && !e.ctrlKey && !e.altKey && !e.metaKey && !e.isComposing) {
        var v2 = ta.value, p = ta.selectionStart;
        var debutL = v2.lastIndexOf("\n", p - 1) + 1, ligne = v2.slice(debutL, p);
        var r = (/^[ \t]*/.exec(ligne) || [""])[0];
        if (/:$/.test(hors_chaines(ligne).trimEnd())) r += "    ";
        if (r) { e.preventDefault(); remplacer(p, ta.selectionEnd, "\n" + r); }
      }
    });

    // ── la console
    var courant = null;
    function viderConsole() { cons.innerHTML = ""; courant = null; derniereSortie = ""; }
    function ecrire(t) {
      if (!courant) { courant = el("span", "editeur-py-sortie"); cons.appendChild(courant); }
      courant.appendChild(document.createTextNode(t));
      derniereSortie += t;
      cons.scrollTop = cons.scrollHeight;
    }
    function info(t, cls) { var d = el("div", "editeur-py-info " + (cls || ""), t); cons.appendChild(d); courant = null; cons.scrollTop = cons.scrollHeight; return d; }
    function lire(invite) {
      return new Promise(function (ok, ko) {
        if (invite) ecrire(invite);
        var ligne = el("span", "editeur-py-entree");
        var champ = el("input", "editeur-py-entree-champ"); champ.type = "text";
        champ.setAttribute("aria-label", "Ta réponse à input() : écris-la, puis Entrée");
        champ.setAttribute("autocomplete", "off"); champ.setAttribute("spellcheck", "false");
        var bOk = bouton("editeur-py-entree-ok", "↵ Valider");
        ligne.appendChild(champ); ligne.appendChild(bOk);
        if (!courant) { courant = el("span", "editeur-py-sortie"); cons.appendChild(courant); }
        courant.appendChild(ligne);
        etat.textContent = "⌨ Ton programme attend ta réponse dans la console (input) : écris-la, puis Entrée.";
        function valider() {
          var v = champ.value;
          ligne.replaceWith(document.createTextNode(""));
          var echo = el("span", "editeur-py-echo", v); courant.appendChild(echo); courant.appendChild(document.createTextNode("\n"));
          derniereSortie += v + "\n";
          etat.textContent = "▶ Ton programme tourne…";
          enCours && (enCours.annulerEntree = null);
          ok(v);
        }
        champ.addEventListener("keydown", function (e) { if (e.key === "Enter") { e.preventDefault(); valider(); } });
        bOk.addEventListener("click", valider);
        if (enCours) enCours.annulerEntree = function () { ligne.remove(); ko(ARRET); };
        setTimeout(function () { try { champ.focus({ preventScroll: false }); } catch (x) { champ.focus(); } }, 0);
      });
    }

    function lancer() {
      if (enCours) return Promise.resolve(null);
      demarquer(); viderConsole();
      bExe.disabled = true; bStop.disabled = false; bloc.classList.add("editeur-py--tourne");
      var premier = !(window.Sk && window.Sk.builtinFiles);
      var attente = premier ? info("⏳ Python se prépare (la première fois seulement)…", "editeur-py-attente") : null;
      etat.textContent = "▶ Ton programme tourne…";
      var signal = {}, t0 = Date.now();
      enCours = signal;
      var code = ta.value;
      return moteur(code, prelude(bloc.getAttribute("data-simulation")), {
        ecrire: function (t) { if (attente) { attente.remove(); attente = null; } ecrire(t); },
        lire: function (inv) { if (attente) { attente.remove(); attente = null; } return lire(inv); },
        signal: signal
      }).then(function (r) {
        if (attente) { attente.remove(); attente = null; }
        var s = ((Date.now() - t0) / 1000).toFixed(1).replace(".", ",");
        if (r.erreur) {
          var b = el("div", "editeur-py-erreur");
          b.appendChild(el("p", "editeur-py-erreur-titre", "⚠ " + r.erreur.titre + (r.erreur.ligne ? " — ligne " + r.erreur.ligne : "")));
          b.appendChild(el("p", "editeur-py-erreur-texte", r.erreur.explication));
          b.appendChild(el("p", "editeur-py-erreur-brut", "Message de Python : " + r.erreur.message));
          cons.appendChild(b); courant = null; cons.scrollTop = cons.scrollHeight;
          derniereSortie += "\n⚠ " + r.erreur.titre + (r.erreur.ligne ? " (ligne " + r.erreur.ligne + ")" : "") + " : " + r.erreur.explication;
          if (r.erreur.ligne) marquer(r.erreur.ligne);
          etat.textContent = "⚠ Ton programme s'est arrêté sur une erreur" + (r.erreur.ligne ? ", ligne " + r.erreur.ligne : "") + " : l'explication est dans la console.";
        } else if (r.arret) {
          var m = r.arret === "bouton" ? "⏹ Arrêté par le bouton ⏹ Arrêter."
            : r.arret === "lignes" ? "⏹ La console débordait (plus de " + LIGNES_MAX + " lignes) : la page a arrêté ton programme. Une boucle qui affiche sans fin ?"
            : "⏹ Ton programme tournait depuis " + LIMITE_TOTALE / 1000 + " secondes : la page l'a arrêté. Un « while True » ne s'arrête jamais tout seul — c'est normal pour un vrai système ; ici, on arrête pour lire la console.";
          info(m, "editeur-py-stop");
          derniereSortie += "\n" + m;
          etat.textContent = m;
        } else {
          if (!r.sortie) info("(ton programme n'a rien affiché : il faut un print(…) pour voir quelque chose)", "editeur-py-rien");
          info("✔ Terminé en " + s + " s.", "editeur-py-fin");
          etat.textContent = "✔ Ton programme s'est exécuté jusqu'au bout (" + s + " s).";
        }
        impSortie.textContent = derniereSortie.trim() ? derniereSortie : "\n\n\n";
        r.code = code;
        return r;
      }, function (err) {
        if (attente) { attente.remove(); attente = null; }
        info("⚠ L'éditeur n'a pas pu démarrer Python (" + (err && err.message || err) + "). Utilise le lien Vittascience, ou recopie ton programme sur ton cahier.", "editeur-py-panne");
        etat.textContent = "⚠ Python n'a pas pu démarrer.";
        return { sortie: "", erreur: { type: "Panne", message: String(err), titre: "Panne", explication: String(err), ligne: null }, arret: null, code: code };
      }).then(function (r) {
        enCours = null;
        bExe.disabled = false; bStop.disabled = true; bloc.classList.remove("editeur-py--tourne");
        bloc.dispatchEvent(new CustomEvent("editeur-py:fin", { bubbles: true, detail: {
          bloc: bloc.id || null, champ: id, code: r.code, sortie: r.sortie, erreur: r.erreur, arret: r.arret } }));
        return r;
      });
    }
    function arreter() {
      if (!enCours) return;
      enCours.arret = true;
      if (enCours.annulerEntree) enCours.annulerEntree();
      if (enCours.interrompre) enCours.interrompre();
    }

    bExe.addEventListener("click", lancer);
    bStop.addEventListener("click", arreter);

    // ↺ en deux clics : on ne perd pas un programme par mégarde
    var armer = null, sauvegardeAvant = null;
    bDep.addEventListener("click", function () {
      if (!armer) {
        bDep.textContent = "↺ Sûr ? Clique encore pour remettre le départ";
        bDep.classList.add("editeur-py-arme");
        armer = setTimeout(function () { armer = null; bDep.textContent = "↺ Remettre le code de départ"; bDep.classList.remove("editeur-py-arme"); }, 4000);
        return;
      }
      clearTimeout(armer); armer = null; bDep.textContent = "↺ Remettre le code de départ"; bDep.classList.remove("editeur-py-arme");
      sauvegardeAvant = ta.value;
      ta.value = depart; demarquer(); majVue(); sauver();
      etat.textContent = "↺ Le code de départ est revenu. ";
      var annuler = bouton("editeur-py-annuler", "↶ Retrouver mon programme");
      etat.appendChild(annuler);
      annuler.addEventListener("click", function () { ta.value = sauvegardeAvant; majVue(); sauver(); etat.textContent = "↶ Ton programme est revenu."; });
    });

    // ⬇ Télécharger : un premier clic rappelle le geste 2 si « TON NOM » est encore là
    var rappelNom = false;
    bTel.addEventListener("click", function () {
      var n = propreNom(nom.value);
      if (/TON NOM/i.test(n) && !rappelNom) {
        rappelNom = true; nom.focus(); nom.select && nom.select();
        etat.textContent = "📄 Écris d'abord ton nom à la place de « TON NOM » dans le nom du fichier (geste 2), puis clique encore ⬇.";
        return;
      }
      rappelNom = false;
      var blob = new Blob([ta.value.replace(/\r?\n/g, "\r\n")], { type: "text/x-python;charset=utf-8" });
      var a = document.createElement("a");
      a.href = URL.createObjectURL(blob); a.download = n + ".py"; a.style.display = "none";
      document.body.appendChild(a); a.click();
      setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 1000);
      etat.textContent = "⬇ « " + n + ".py » part dans ton dossier Téléchargements. Range-le maintenant dans Documents › ta classe (geste 3).";
    });
    nom.addEventListener("input", function () { rappelNom = false; });

    // 📂 Ouvrir : le sélecteur de fichier du navigateur
    bOuv.addEventListener("click", function () { choix.value = ""; choix.click(); });
    choix.addEventListener("change", function () {
      var f = choix.files && choix.files[0]; if (!f) return;
      var lecteur = new FileReader();
      lecteur.onload = function () {
        var texte = String(lecteur.result || "").replace(/\r\n?/g, "\n").replace(/^﻿/, "");
        var entete = /^\s*("""|''')[\s\S]*?\1\s*\n/.exec(texte), retire = false;
        if (entete && /vittascience/i.test(entete[0])) { texte = texte.slice(entete[0].length).replace(/^\n+/, ""); retire = true; }
        sauvegardeAvant = ta.value;
        ta.value = texte.replace(/\n+$/, "") + (texte ? "\n" : "");
        demarquer(); majVue(); sauver();
        var base = f.name.replace(/\.py$/i, "");
        if (base) { nom.value = base; nom.dispatchEvent(new Event("change", { bubbles: true })); }
        etat.textContent = "📂 « " + f.name + " » est ouvert : ton programme est revenu dans l'éditeur" + (retire ? " (l'en-tête de Vittascience a été retiré)." : ".");
      };
      lecteur.onerror = function () { etat.textContent = "⚠ Ce fichier n'a pas pu être lu."; };
      lecteur.readAsText(f, "utf-8");
    });

    // Sans programme sauvegardé, le champ garde le code de départ ; sinon la page l'a déjà remis (ou le remettra).
    if (!ta.value && depart) ta.value = depart;
    majVue();

    instances[id] = {
      bloc: bloc, champ: ta,
      executer: lancer, arreter: arreter,
      get code() { return ta.value; }, set code(v) { ta.value = v; majVue(); sauver(); },
      sortie: function () { return derniereSortie; },
      depart: depart
    };
  }

  function monterTout() { [].forEach.call(document.querySelectorAll(".editeur-py"), monter); }

  window.EditeurPython = {
    executer: executer,
    instance: function (id) { return instances[id] || null; },
    instances: instances,
    monter: monterTout,
    charger: chargerSkulpt,
    _decrire: decrire,
    LIMITE_ACTIVE: LIMITE_ACTIVE, LIMITE_TOTALE: LIMITE_TOTALE, LIGNES_MAX: LIGNES_MAX
  };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", monterTout);
  else monterTout();
})();
