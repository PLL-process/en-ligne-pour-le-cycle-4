/* banc_python.js — un petit Python qui s'exécute dans la page, sans réseau (règle d'or n°305).
 *
 * POURQUOI (audit de « Programmer l'alerte », 3e_C6.1, 21/11/2026)
 * Le bouton « Vérifier » de l'activité 4 cherchait des motifs dans le TEXTE du programme : un programme juste écrit
 * avec des apostrophes obtenait 5 / 7 et le conseil de réparer deux branches justes ; un programme faux à 118 km/h
 * (`>=` au lieu de `>`) obtenait 7 / 7. Une validation de programme regarde ce que le programme FAIT : on l'exécute
 * sur des entrées fictives et on compare ses sorties au cahier des charges (règle d'or n°333 : une autre solution juste est acceptée, on compare le comportement, pas le texte).
 *
 * CE QU'IL EXÉCUTE — le Python d'un programme de collège, un passage, sans boucle :
 *   affectations (`x = …`, `x += …`), `if` / `elif` / `else` avec l'indentation, `pass`,
 *   nombres entiers et décimaux, textes entre "…" ou '…', True / False / None,
 *   + - * / // % , comparaisons (enchaînées comprises), and / or / not, parenthèses,
 *   appels des fonctions que la page fournit (capteurs, envoi, actionneurs) et de print, float, int, str, input,
 *   abs, round, min, max.
 * CE QU'IL REFUSE, EN LE DISANT : while, for, def, import, return, les listes — « le banc de la page ne sait pas
 *   encore exécuter … » (une limite dite n'est pas une erreur de l'élève).
 * LES ERREURS : celles de Python, avec leur nom anglais (IndentationError, SyntaxError, NameError, TypeError),
 *   la ligne, et une phrase en français qui dit quoi regarder.
 * LA TRACE : chaque test évalué (« ligne 12 · vent_kmh > SEUIL_OURAGAN → 118 > 118 → faux »), chaque affectation,
 *   chaque appel : c'est le chemin suivi que l'élève peut dérouler pas à pas.
 *
 * Source unique : _outils/banc_python/ (poser.py le pose dans une page, entre ses marqueurs). Banc :
 * _outils/banc_python/tests_banc_python.mjs.
 */
(function (global) {
  "use strict";

  function Erreur(type, ligne, message, conseil) {
    this.type = type; this.ligne = ligne; this.message = message; this.conseil = conseil || "";
  }

  /* ───── valeurs Python ───── */
  var NONE = { t: "none" };
  function vInt(n) { return { t: "int", v: n }; }
  function vFloat(n) { return { t: "float", v: n }; }
  function vStr(s) { return { t: "str", v: s }; }
  function vBool(b) { return { t: "bool", v: !!b }; }
  function estNombre(x) { return x.t === "int" || x.t === "float" || x.t === "bool"; }
  function nombre(x) { return x.t === "bool" ? (x.v ? 1 : 0) : x.v; }
  function nomType(x) { return { int: "int", float: "float", str: "str", bool: "bool", none: "NoneType" }[x.t] || x.t; }
  function repr(x) {
    if (x.t === "str") return JSON.stringify(x.v).replace(/^"|"$/g, '"');
    return texte(x);
  }
  function texte(x) {
    if (x.t === "str") return x.v;
    if (x.t === "bool") return x.v ? "True" : "False";
    if (x.t === "none") return "None";
    if (x.t === "float") {
      if (!isFinite(x.v)) return x.v > 0 ? "inf" : "-inf";
      return Number.isInteger(x.v) ? x.v.toFixed(1) : String(x.v);
    }
    return String(x.v);
  }
  function vrai(x) {
    if (x.t === "none") return false;
    if (x.t === "str") return x.v.length > 0;
    return nombre(x) !== 0;
  }

  /* ───── découpe en lignes logiques ───── */
  var MOTS = { "if": 1, "elif": 1, "else": 1, "and": 1, "or": 1, "not": 1, "True": 1, "False": 1, "None": 1, "pass": 1,
    "while": 1, "for": 1, "def": 1, "import": 1, "from": 1, "return": 1, "in": 1, "is": 1, "class": 1, "lambda": 1,
    "break": 1, "continue": 1, "with": 1, "try": 1, "except": 1, "global": 1 };
  var OPS = ["**", "//", "==", "!=", ">=", "<=", "+=", "-=", "*=", "/=", ">", "<", "=", "+", "-", "*", "/", "%", "(", ")", ",", ":", "[", "]", ".", "{", "}", ";"];

  /* un texte entre guillemets, depuis son guillemet ouvrant ; brut (r"…") : sans séquences \n */
  function lireTexte(ligne, i, n, brut) {
    var q = ligne[i], j = i + 1, s = "", L = ligne.length;
    if (ligne.substr(i, 3) === q + q + q) throw new Erreur("SyntaxError", n, "texte sur plusieurs lignes (''' ou \"\"\")",
      "le banc de la page lit les textes d'une seule ligne : écris \"…\" ou '…'.");
    while (j < L && ligne[j] !== q) {
      if (ligne[j] === "\\" && j + 1 < L) { var e = ligne[j + 1]; s += brut ? "\\" + e : (e === "n" ? "\n" : e === "t" ? "\t" : e); j += 2; continue; }
      s += ligne[j]; j++;
    }
    if (j >= L) throw new Erreur("SyntaxError", n, "unterminated string literal", "un texte commence par " + q + " mais ne se ferme pas : ajoute le " + q + " de fin.");
    return { s: s, fin: j + 1 };
  }

  function decouper(ligne, n) {
    var toks = [], i = 0, L = ligne.length;
    while (i < L) {
      var c = ligne[i];
      if (c === " " || c === "\t") { i++; continue; }
      if (c === "#") break;
      var pref = /^([fFrRuUbB]{1,2})(?=["'])/.exec(ligne.slice(i));
      if (pref && !/[A-Za-z_À-ÿ0-9]/.test(ligne[i - 1] || "")) {
        var p = pref[1].toLowerCase();
        if (p.indexOf("b") >= 0) throw new Erreur("NonPrisEnCharge", n, "les octets (b\"…\")", "le banc de la page lit les textes ordinaires \"…\" : ton programme est peut-être juste en Python, essaie-le sur ordinateur (Bonus).");
        var lu = lireTexte(ligne, i + p.length, n, p.indexOf("r") >= 0);
        toks.push({ k: p.indexOf("f") >= 0 ? "fstr" : "str", v: lu.s, n: n }); i = lu.fin; continue;
      }
      if (c === '"' || c === "'") {
        var q = c, j = i + 1, s = "";
        if (ligne.substr(i, 3) === q + q + q) throw new Erreur("SyntaxError", n, "texte sur plusieurs lignes (''' ou \"\"\")",
          "le banc de la page lit les textes d'une seule ligne : écris \"…\" ou '…'.");
        while (j < L && ligne[j] !== q) {
          if (ligne[j] === "\\" && j + 1 < L) {
            var e = ligne[j + 1];
            s += e === "n" ? "\n" : e === "t" ? "\t" : e;
            j += 2; continue;
          }
          s += ligne[j]; j++;
        }
        if (j >= L) throw new Erreur("SyntaxError", n, "unterminated string literal",
          "un texte commence par " + q + " mais ne se ferme pas : ajoute le " + q + " de fin.");
        toks.push({ k: "str", v: s, n: n }); i = j + 1; continue;
      }
      if (/[0-9]/.test(c) || (c === "." && /[0-9]/.test(ligne[i + 1] || ""))) {
        var m = /^(\d+\.\d*|\.\d+|\d+)([eE][+-]?\d+)?/.exec(ligne.slice(i));
        var brut = m[0];
        var estDec = brut.indexOf(".") >= 0 || /[eE]/.test(brut);
        if (/^[A-Za-z_]/.test(ligne.slice(i + brut.length))) throw new Erreur("SyntaxError", n, "invalid decimal literal",
          "un nombre est collé à des lettres (« " + ligne.slice(i, i + brut.length + 3).trim() + "… ») : sépare-les.");
        toks.push({ k: "num", v: estDec ? vFloat(parseFloat(brut)) : vInt(parseInt(brut, 10)), brut: brut, n: n });
        i += brut.length; continue;
      }
      if (/[A-Za-z_À-ÿ]/.test(c)) {
        var mn = /^[A-Za-z_À-ÿ][A-Za-z0-9_À-ÿ]*/.exec(ligne.slice(i))[0];
        toks.push({ k: MOTS[mn] ? "mot" : "nom", v: mn, n: n }); i += mn.length; continue;
      }
      var op = null;
      for (var o = 0; o < OPS.length; o++) if (ligne.substr(i, OPS[o].length) === OPS[o]) { op = OPS[o]; break; }
      if (op === null) {
        var conseil = c === "≥" || c === "≤" || c === "≠" ? "en Python, on écrit " + ({ "≥": ">=", "≤": "<=", "≠": "!=" })[c] + " avec deux caractères."
          : c === "«" || c === "»" || c === "“" || c === "”" ? "les guillemets d'un texte Python sont \" ou ' (pas « » ni “ ”)."
          : "ce caractère n'existe pas en Python.";
        throw new Erreur("SyntaxError", n, "invalid character '" + c + "'", conseil);
      }
      toks.push({ k: "op", v: op, n: n }); i += op.length;
    }
    return toks;
  }

  function lignesLogiques(code) {
    var brutes = String(code).replace(/\r\n?/g, "\n").split("\n"), out = [];
    for (var i = 0; i < brutes.length; i++) {
      var l = brutes[i], n = i + 1;
      var m = /^[ \t]*/.exec(l)[0];
      var toks = decouper(l, n);
      if (!toks.length) continue;
      var largeur = 0;
      for (var j = 0; j < m.length; j++) largeur = m[j] === "\t" ? (Math.floor(largeur / 8) + 1) * 8 : largeur + 1;
      var prof = 0;
      toks.forEach(function (t) { if (t.k === "op" && (t.v === "(" || t.v === "[")) prof++; if (t.k === "op" && (t.v === ")" || t.v === "]")) prof--; });
      if (prof > 0) throw new Erreur("SyntaxError", n, "'(' was never closed", "une parenthèse ouverte sur cette ligne n'est pas refermée.");
      if (prof < 0) throw new Erreur("SyntaxError", n, "unmatched ')'", "une parenthèse fermante n'a pas d'ouvrante.");
      var morceaux = [[]];
      toks.forEach(function (t) { if (t.k === "op" && t.v === ";") morceaux.push([]); else morceaux[morceaux.length - 1].push(t); });
      if (morceaux.length > 1) {
        var t0 = toks[0];
        if (t0.k === "mot" && /^(if|elif|else|while|for|def|class|try|with)$/.test(t0.v)) throw new Erreur("NonPrisEnCharge", n, "plusieurs instructions sur une ligne « " + t0.v + " »",
          "le banc de la page lit une instruction par ligne après « " + t0.v + " » : ton programme est peut-être juste en Python ; va à la ligne pour l'essayer ici.");
        morceaux = morceaux.filter(function (m) { return m.length; });
        morceaux.forEach(function (m) { out.push({ n: n, retrait: largeur, toks: m, source: l.trim() }); });
        continue;
      }
      out.push({ n: n, retrait: largeur, toks: toks, source: l.trim() });
    }
    return out;
  }

  /* ───── analyse : les blocs, puis les instructions ───── */
  function Analyseur(toks, n) { this.t = toks; this.i = 0; this.n = n; }
  Analyseur.prototype = {
    voir: function () { return this.t[this.i]; },
    est: function (k, v) { var x = this.t[this.i]; return !!x && x.k === k && (v === undefined || x.v === v); },
    prendre: function (k, v) {
      var x = this.t[this.i];
      if (!x || x.k !== k || (v !== undefined && x.v !== v)) {
        var vu = x ? "« " + x.v + " »" : "la fin de la ligne";
        throw new Erreur("SyntaxError", this.n, "invalid syntax", "j'attendais « " + (v || k) + " » et je lis " + vu + ".");
      }
      this.i++; return x;
    },
    fin: function () { return this.i >= this.t.length; },
    expr: function () {
      var g = this.ou();
      if (this.est("mot", "if")) {
        this.i++; var c = this.ou();
        if (!this.est("mot", "else")) throw new Erreur("SyntaxError", this.n, "expected 'else' after 'if' expression", "« valeur if test » demande aussi « else autre_valeur ».");
        this.i++; return { k: "tern", c: c, g: g, d: this.expr() };
      }
      return g;
    },
    ou: function () {
      var g = this.et();
      while (this.est("mot", "or")) { this.i++; g = { k: "ou", g: g, d: this.et() }; }
      return g;
    },
    et: function () {
      var g = this.non();
      while (this.est("mot", "and")) { this.i++; g = { k: "et", g: g, d: this.non() }; }
      return g;
    },
    non: function () {
      if (this.est("mot", "not")) { this.i++; return { k: "non", x: this.non() }; }
      return this.comparaison();
    },
    comparaison: function () {
      var g = this.somme(), ops = [], termes = [g];
      while (true) {
        if (this.est("op", ">") || this.est("op", "<") || this.est("op", ">=") || this.est("op", "<=") || this.est("op", "==") || this.est("op", "!=")) { ops.push(this.voir().v); this.i++; }
        else if (this.est("mot", "is")) { this.i++; if (this.est("mot", "not")) { this.i++; ops.push("is not"); } else ops.push("is"); }
        else if (this.est("mot", "in")) { this.i++; ops.push("in"); }
        else if (this.est("mot", "not") && this.t[this.i + 1] && this.t[this.i + 1].k === "mot" && this.t[this.i + 1].v === "in") { this.i += 2; ops.push("not in"); }
        else break;
        termes.push(this.somme());
      }
      if (this.est("op", "=")) throw new Erreur("SyntaxError", this.n, "invalid syntax. Maybe you meant '==' or ':=' instead of '='?",
        "dans un test, on compare avec == (deux signes égal) ; un seul = range une valeur dans une variable.");
      return ops.length ? { k: "cmp", ops: ops, termes: termes } : g;
    },
    somme: function () {
      var g = this.produit();
      while (this.est("op", "+") || this.est("op", "-")) { var o = this.voir().v; this.i++; g = { k: "bin", op: o, g: g, d: this.produit() }; }
      return g;
    },
    produit: function () {
      var g = this.unaire();
      while (this.est("op", "*") || this.est("op", "/") || this.est("op", "//") || this.est("op", "%")) { var o = this.voir().v; this.i++; g = { k: "bin", op: o, g: g, d: this.unaire() }; }
      return g;
    },
    unaire: function () {
      if (this.est("op", "-")) { this.i++; return { k: "neg", x: this.unaire() }; }
      if (this.est("op", "+")) { this.i++; return this.unaire(); }
      return this.puissance();
    },
    puissance: function () {
      var g = this.primaire();
      if (this.est("op", "**")) { this.i++; return { k: "bin", op: "**", g: g, d: this.unaire() }; }
      return g;
    },
    primaire: function () {
      var x = this.voir();
      if (!x) throw new Erreur("SyntaxError", this.n, "invalid syntax", "la ligne s'arrête avant la fin de l'expression.");
      if (x.k === "num") { this.i++; return { k: "lit", v: x.v, src: x.brut }; }
      if (x.k === "str") { this.i++; return { k: "lit", v: vStr(x.v), src: repr(vStr(x.v)) }; }
      if (x.k === "fstr") { this.i++; return { k: "fstr", parts: morceauxF(x.v, this.n), src: "f" + repr(vStr(x.v)) }; }
      if (x.k === "mot" && (x.v === "True" || x.v === "False")) { this.i++; return { k: "lit", v: vBool(x.v === "True"), src: x.v }; }
      if (x.k === "mot" && x.v === "None") { this.i++; return { k: "lit", v: NONE, src: "None" }; }
      if (x.k === "op" && x.v === "(") {
        this.i++; var e = this.expr(); this.prendre("op", ")"); return { k: "par", x: e };
      }
      if (x.k === "nom") {
        this.i++;
        if (this.est("op", "(")) {
          this.i++; var args = [];
          if (!this.est("op", ")")) {
            args.push(this.expr());
            while (this.est("op", ",")) { this.i++; if (this.est("op", ")")) break; args.push(this.expr()); }
          }
          this.prendre("op", ")");
          return { k: "appel", nom: x.v, args: args };
        }
        if (this.est("op", "[") || this.est("op", ".")) throw new Erreur("NonPrisEnCharge", this.n, "listes et méthodes",
          "le banc de la page ne sait pas encore exécuter les listes ni les méthodes (« " + x.v + this.voir().v + " »).");
        return { k: "nom", nom: x.v };
      }
      if (x.k === "mot" && (x.v === "true" || x.v === "false")) throw new Erreur("NameError", this.n, "name '" + x.v + "' is not defined", "");
      if (x.k === "op" && x.v === "[") throw new Erreur("NonPrisEnCharge", this.n, "listes", "le banc de la page ne sait pas encore exécuter les listes.");
      if (x.k === "op" && x.v === "{") throw new Erreur("NonPrisEnCharge", this.n, "dictionnaires et ensembles { }", "le banc de la page ne sait pas encore exécuter { } : ton programme est peut-être juste en Python, essaie-le sur ordinateur (Bonus).");
      if (x.k === "mot" && MOTS_INCONNUS[x.v]) throw nonLu(x.v, this.n);
      throw new Erreur("SyntaxError", this.n, "invalid syntax", "je ne m'attendais pas à lire « " + x.v + " » ici.");
    }
  };

  /* mots de Python que le banc ne lit pas à cet endroit : jamais une « SyntaxError » pour un programme peut-être juste */
  var MOTS_INCONNUS = { "lambda": 1, "yield": 1, "await": 1, "async": 1, "del": 1, "assert": 1, "raise": 1, "nonlocal": 1, "global": 1, "for": 1, "in": 1, "is": 1, "while": 1, "with": 1, "as": 1 };
  function nonLu(mot, n) {
    return new Erreur("NonPrisEnCharge", n, "« " + mot + " » à cet endroit",
      "le banc de la page ne lit pas cette écriture : ton programme est peut-être juste en Python. Essaie-le dans Python sur ordinateur (Bonus), ou écris cette ligne plus simplement.");
  }
  /* f"Vigilance {vigilance}" : les morceaux de texte et les expressions entre accolades */
  function morceauxF(s, n) {
    var parts = [], i = 0, cur = "";
    while (i < s.length) {
      var c = s[i];
      if (c === "{" && s[i + 1] === "{") { cur += "{"; i += 2; continue; }
      if (c === "}" && s[i + 1] === "}") { cur += "}"; i += 2; continue; }
      if (c === "{") {
        var j = s.indexOf("}", i);
        if (j < 0) throw new Erreur("SyntaxError", n, "f-string: expecting '}'", "une accolade { ouverte dans le texte n'est pas refermée.");
        var dedans = s.slice(i + 1, j);
        if (/[:!]/.test(dedans.replace(/(["'])(?:(?!\1).)*\1/g, "")) || /=\s*$/.test(dedans)) throw new Erreur("NonPrisEnCharge", n, "les f-strings avec un format ({…:…})",
          "le banc de la page lit f\"…{nom}…\" sans format : ton programme est peut-être juste en Python, essaie-le sur ordinateur (Bonus).");
        if (cur) parts.push(cur); cur = "";
        var a = new Analyseur(decouper(dedans, n), n), e = a.expr();
        if (!a.fin()) throw new Erreur("SyntaxError", n, "f-string: invalid syntax", "entre accolades, une seule expression.");
        parts.push(e); i = j + 1; continue;
      }
      if (c === "}") throw new Erreur("SyntaxError", n, "f-string: single '}' is not allowed", "une accolade } seule : double-la (}}) pour l'écrire.");
      cur += c; i++;
    }
    if (cur) parts.push(cur);
    return parts;
  }

  var NON_PRIS = { "while": "les boucles while", "for": "les boucles for", "def": "les fonctions (def)", "import": "import", "from": "import",
    "return": "return", "class": "les classes", "try": "try", "with": "with", "lambda": "lambda", "break": "break", "continue": "continue", "global": "global" };

  function instruction(ll) {
    var a = new Analyseur(ll.toks, ll.n), t0 = ll.toks[0];
    if (t0.k === "mot" && NON_PRIS[t0.v]) {
      var conseil = t0.v === "while" ? "le banc exécute UN passage du programme, comme une mesure de la station : retire « while » pour l'essayer ici, ou essaie ce programme dans Python sur ordinateur (Bonus)."
        : "le banc de la page ne sait pas encore exécuter " + NON_PRIS[t0.v] + " : essaie ce programme dans Python sur ordinateur (Bonus).";
      throw new Erreur("NonPrisEnCharge", ll.n, NON_PRIS[t0.v], conseil);
    }
    if (t0.k === "mot" && (t0.v === "if" || t0.v === "elif")) {
      a.i++;
      if (a.fin() || a.est("op", ":")) throw new Erreur("SyntaxError", ll.n, "invalid syntax", "« " + t0.v + " » doit être suivi d'un test, par exemple « " + t0.v + " vent_kmh > SEUIL_ROUGE: ».");
      var test = a.expr();
      if (!a.est("op", ":")) {
        if (a.voir() && a.voir().k === "mot" && MOTS_INCONNUS[a.voir().v]) throw nonLu(a.voir().v, ll.n);
        throw new Erreur("SyntaxError", ll.n, "expected ':'", "une ligne « " + t0.v + " … » se termine par deux-points « : ».");
      }
      a.i++;
      var reste = a.fin() ? null : instructionSimple(a, ll);
      return { k: t0.v, test: test, n: ll.n, src: sourceTest(ll), seule: reste };
    }
    if (t0.k === "mot" && t0.v === "else") {
      a.i++;
      if (a.est("nom") || a.est("mot", "if")) throw new Erreur("SyntaxError", ll.n, "expected ':'", "en Python, « sinon si » s'écrit elif, en un seul mot.");
      a.prendre("op", ":");
      var r2 = a.fin() ? null : instructionSimple(a, ll);
      return { k: "else", n: ll.n, seule: r2 };
    }
    var ins = instructionSimple(a, ll);
    return ins;
  }
  function sourceTest(ll) {
    var s = ll.source.replace(/^(if|elif)\s+/, "");
    var c = s.lastIndexOf(":"); if (c >= 0) s = s.slice(0, c);
    var h = s.indexOf("#"); if (h >= 0) s = s.slice(0, h);
    return s.trim();
  }
  function instructionSimple(a, ll) {
    if (a.est("mot", "pass")) { a.i++; finDeLigne(a, ll); return { k: "pass", n: ll.n }; }
    if (a.est("nom") && a.t[a.i + 1] && a.t[a.i + 1].k === "op" && /^(=|\+=|-=|\*=|\/=)$/.test(a.t[a.i + 1].v)) {
      var nom = a.voir().v, op = a.t[a.i + 1].v; a.i += 2;
      if (a.fin()) throw new Erreur("SyntaxError", ll.n, "invalid syntax", "rien n'est écrit après « " + nom + " " + op + " ».");
      var e = a.expr(); finDeLigne(a, ll);
      return { k: "affecte", nom: nom, op: op, x: e, n: ll.n };
    }
    if (a.est("mot") && /^(True|False|None)$/.test(a.voir().v) && a.t[a.i + 1] && a.t[a.i + 1].v === "=")
      throw new Erreur("SyntaxError", ll.n, "cannot assign to " + a.voir().v, "");
    var x = a.expr(); finDeLigne(a, ll);
    return { k: "expr", x: x, n: ll.n };
  }
  function finDeLigne(a, ll) {
    if (!a.fin()) {
      var t = a.voir();
      if (t.k === "op" && t.v === ":") throw new Erreur("SyntaxError", ll.n, "invalid syntax", "deux-points « : » en trop : seules les lignes if, elif et else en portent.");
      if (t.k === "mot" && MOTS_INCONNUS[t.v]) throw nonLu(t.v, ll.n);
      throw new Erreur("SyntaxError", ll.n, "invalid syntax", "je lis encore « " + t.v + " » après la fin de l'instruction.");
    }
  }

  function construire(lignes) {
    var pos = 0;
    function bloc(retrait, parent) {
      var corps = [];
      while (pos < lignes.length) {
        var ll = lignes[pos];
        if (ll.retrait < retrait) break;
        if (ll.retrait > retrait) throw new Erreur("IndentationError", ll.n, "unexpected indent",
          "cette ligne est plus décalée que la précédente sans qu'un if, elif ou else ne l'ait annoncé : retire les espaces en trop.");
        var ins = instruction(ll); pos++;
        if (ins.k === "if" || ins.k === "elif" || ins.k === "else") {
          if (ins.seule) { ins.corps = [ins.seule]; }
          else {
            if (pos >= lignes.length || lignes[pos].retrait <= retrait) {
              var ligneAttendue = pos < lignes.length ? lignes[pos].n : ll.n + 1;
              throw new Erreur("IndentationError", ligneAttendue, "expected an indented block after '" + ins.k + "' statement on line " + ll.n,
                "après « " + ll.source + " », Python attend au moins une ligne décalée de 4 espaces.");
            }
            var interieur = lignes[pos].retrait;
            ins.corps = bloc(interieur, ins);
            if (pos < lignes.length && lignes[pos].retrait > retrait && lignes[pos].retrait < interieur)
              throw new Erreur("IndentationError", lignes[pos].n, "unindent does not match any outer indentation level",
                "cette ligne ne s'aligne sur aucun bloc : aligne-la sur le if dont elle dépend, ou sur les lignes de sa branche.");
          }
          if (ins.k === "if") corps.push({ k: "si", branches: [ins] });
          else {
            var der = corps[corps.length - 1];
            if (!der || der.k !== "si" || der.ferme) throw new Erreur("SyntaxError", ll.n, "invalid syntax",
              "« " + ins.k + " » doit suivre un if (ou un elif) au même décalage.");
            der.branches.push(ins); if (ins.k === "else") der.ferme = true;
          }
        } else corps.push(ins);
      }
      return corps;
    }
    if (lignes.length && lignes[0].retrait > 0) throw new Erreur("IndentationError", lignes[0].n, "unexpected indent", "la première instruction du programme commence au bord gauche, sans espaces.");
    var prog = bloc(0, null);
    if (pos < lignes.length) throw new Erreur("IndentationError", lignes[pos].n, "unindent does not match any outer indentation level", "");
    return prog;
  }

  /* ───── exécution ───── */
  function Machine(options) {
    this.vars = Object.create(null);
    this.trace = [];
    this.sorties = { messages: [], affichages: [], appels: [] };
    this.fonctions = Object.create(null);
    var self = this, o = options || {};
    var f = this.fonctions;
    f.print = function (args) { self.sorties.affichages.push(args.map(texte).join(" ")); return NONE; };
    f.float = function (args, n) { unArg("float", args, n); var x = args[0];
      if (x.t === "str") { var s = x.v.trim(); if (!/^[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?$/.test(s)) throw new Erreur("ValueError", n, "could not convert string to float: " + repr(x), /^\s*[+-]?\d+,\d+\s*$/.test(x.v) ? "en Python, un nombre décimal s'écrit avec un point : " + x.v.trim().replace(",", ".") + "." : ""); return vFloat(parseFloat(s)); }
      if (estNombre(x)) return vFloat(nombre(x));
      throw new Erreur("TypeError", n, "float() argument must be a string or a real number, not '" + nomType(x) + "'", ""); };
    f.int = function (args, n) { unArg("int", args, n); var x = args[0];
      if (x.t === "str") { if (!/^\s*[+-]?\d+\s*$/.test(x.v)) throw new Erreur("ValueError", n, "invalid literal for int() with base 10: " + repr(x), ""); return vInt(parseInt(x.v, 10)); }
      if (estNombre(x)) return vInt(Math.trunc(nombre(x)));
      throw new Erreur("TypeError", n, "int() argument must be a string or a number, not '" + nomType(x) + "'", ""); };
    f.str = function (args, n) { unArg("str", args, n); return vStr(texte(args[0])); };
    f.abs = function (args, n) { unArg("abs", args, n); var x = args[0]; if (!estNombre(x)) throw new Erreur("TypeError", n, "bad operand type for abs(): '" + nomType(x) + "'", ""); return x.t === "float" ? vFloat(Math.abs(x.v)) : vInt(Math.abs(nombre(x))); };
    f.round = function (args, n) { var x = args[0]; if (!x || !estNombre(x)) throw new Erreur("TypeError", n, "round() attend un nombre", ""); if (args[1]) { var p = Math.pow(10, nombre(args[1])); return vFloat(Math.round(nombre(x) * p) / p); } return vInt(Math.round(nombre(x))); };
    f.min = function (args, n) { return extremum(args, n, -1); };
    f.max = function (args, n) { return extremum(args, n, 1); };
    f.input = function (args) { var e = o.entrees || []; var k = self._entree = (self._entree || 0); self._entree++; return vStr(e.length ? String(e[Math.min(k, e.length - 1)]) : ""); };
    Object.keys(o.fonctions || {}).forEach(function (nom) {
      f[nom] = function (args, n) {
        var r = o.fonctions[nom](args.map(function (a) { return a.t === "none" ? null : a.v; }), n, self);
        self.sorties.appels.push({ nom: nom, args: args.map(repr), n: n });
        if (r === undefined || r === null) return NONE;
        if (typeof r === "number") return Number.isInteger(r) && !(o.decimaux && o.decimaux[nom]) ? vInt(r) : vFloat(r);
        if (typeof r === "string") return vStr(r);
        if (typeof r === "boolean") return vBool(r);
        return r;
      };
      f[nom].arite = o.arites && o.arites[nom];
    });
    function unArg(nom, args, n) { if (args.length !== 1) throw new Erreur("TypeError", n, nom + "() takes exactly one argument (" + args.length + " given)", ""); }
    function extremum(args, n, s) {
      if (!args.length) throw new Erreur("TypeError", n, "expected at least 1 argument", "");
      var m = args[0];
      args.forEach(function (x) { if (!estNombre(x)) throw new Erreur("TypeError", n, "comparaison impossible avec un texte", ""); if (s * (nombre(x) - nombre(m)) > 0) m = x; });
      return m;
    }
  }
  Machine.prototype = {
    note: function (e) { if (this.trace.length < 2000) this.trace.push(e); },
    eval: function (x, n) {
      var self = this;
      switch (x.k) {
        case "lit": return x.v;
        case "par": return this.eval(x.x, n);
        case "nom":
          if (x.nom in this.vars) return this.vars[x.nom];
          if (this.fonctions[x.nom]) throw new Erreur("TypeError", n, "« " + x.nom + " » est une fonction", "pour l'appeler, ajoute des parenthèses : " + x.nom + "().");
          throw new Erreur("NameError", n, "name '" + x.nom + "' is not defined",
            x.nom === "true" || x.nom === "false" ? "en Python, on écrit " + (x.nom === "true" ? "True" : "False") + " avec une majuscule."
            : "à la ligne " + n + ", « " + x.nom + " » n'a encore reçu aucune valeur : vérifie son orthographe, et qu'une ligne plus haut lui en donne une (même au repos).");
        case "neg": { var v = this.eval(x.x, n); if (!estNombre(v)) throw new Erreur("TypeError", n, "bad operand type for unary -: '" + nomType(v) + "'", ""); return v.t === "float" ? vFloat(-v.v) : vInt(-nombre(v)); }
        case "non": return vBool(!vrai(this.eval(x.x, n)));
        case "et": { var g = this.eval(x.g, n); return vrai(g) ? this.eval(x.d, n) : g; }
        case "ou": { var g2 = this.eval(x.g, n); return vrai(g2) ? g2 : this.eval(x.d, n); }
        case "bin": return this.binaire(x.op, this.eval(x.g, n), this.eval(x.d, n), n);
        case "tern": return vrai(this.eval(x.c, n)) ? this.eval(x.g, n) : this.eval(x.d, n);
        case "fstr": return vStr(x.parts.map(function (p) { return typeof p === "string" ? p : texte(self.eval(p, n)); }).join(""));
        case "cmp": {
          var gauche = this.eval(x.termes[0], n), res = true;
          for (var i = 0; i < x.ops.length; i++) {
            var droite = this.eval(x.termes[i + 1], n);
            res = this.compare(x.ops[i], gauche, droite, n);
            if (!res) break;
            gauche = droite;
          }
          return vBool(res);
        }
        case "appel": {
          var f = this.fonctions[x.nom];
          if (!f) {
            if (x.nom in this.vars) throw new Erreur("TypeError", n, "'" + nomType(this.vars[x.nom]) + "' object is not callable", "");
            throw new Erreur("NameError", n, "name '" + x.nom + "' is not defined", "la fonction « " + x.nom + " » n'existe pas dans la station : vérifie son orthographe (" + Object.keys(this.fonctions).filter(function (k) { return !/^(print|float|int|str|input|abs|round|min|max)$/.test(k); }).join(", ") + ").");
          }
          var args = x.args.map(function (a) { return self.eval(a, n); });
          if (f.arite !== undefined && f.arite !== null && args.length !== f.arite) throw new Erreur("TypeError", n,
            x.nom + "() takes " + f.arite + " positional argument" + (f.arite > 1 ? "s" : "") + " but " + args.length + " " + (args.length > 1 ? "were" : "was") + " given",
            f.arite === 0 ? "« " + x.nom + "() » s'écrit avec des parenthèses vides." : "");
          var r = f(args, n);
          this.note({ t: "appel", n: n, nom: x.nom, args: args.map(repr) });
          return r;
        }
      }
      throw new Erreur("SyntaxError", n, "invalid syntax", "");
    },
    binaire: function (op, a, b, n) {
      if (op === "+" && a.t === "str" && b.t === "str") return vStr(a.v + b.v);
      if (op === "*" && a.t === "str" && (b.t === "int" || b.t === "bool")) return vStr(new Array(Math.max(0, nombre(b)) + 1).join(a.v));
      if (!estNombre(a) || !estNombre(b)) {
        if (op === "+" && a.t === "str") throw new Erreur("TypeError", n, 'can only concatenate str (not "' + nomType(b) + '") to str', "pour coller un nombre à un texte, transforme-le d'abord : str(" + "…" + ").");
        throw new Erreur("TypeError", n, "unsupported operand type(s) for " + op + ": '" + nomType(a) + "' and '" + nomType(b) + "'", "");
      }
      var x = nombre(a), y = nombre(b), flottant = a.t === "float" || b.t === "float";
      switch (op) {
        case "+": return flottant ? vFloat(x + y) : vInt(x + y);
        case "-": return flottant ? vFloat(x - y) : vInt(x - y);
        case "*": return flottant ? vFloat(x * y) : vInt(x * y);
        case "/": if (y === 0) throw new Erreur("ZeroDivisionError", n, "division by zero", ""); return vFloat(x / y);
        case "//": if (y === 0) throw new Erreur("ZeroDivisionError", n, "integer division or modulo by zero", ""); return flottant ? vFloat(Math.floor(x / y)) : vInt(Math.floor(x / y));
        case "%": if (y === 0) throw new Erreur("ZeroDivisionError", n, "integer modulo by zero", ""); var m = x - Math.floor(x / y) * y; return flottant ? vFloat(m) : vInt(m);
        case "**": return flottant || y < 0 ? vFloat(Math.pow(x, y)) : vInt(Math.pow(x, y));
      }
      throw new Erreur("SyntaxError", n, "invalid syntax", "");
    },
    compare: function (op, a, b, n) {
      if (op === "is" || op === "is not") {
        var meme = a.t === b.t && (a.t === "none" || a.v === b.v);
        return op === "is" ? meme : !meme;
      }
      if (op === "in" || op === "not in") {
        if (a.t !== "str" || b.t !== "str") throw new Erreur("NonPrisEnCharge", n, "« in » hors des textes", "le banc de la page sait chercher un texte dans un texte (\"rouge\" in message), pas encore dans une liste.");
        var dans = b.v.indexOf(a.v) >= 0;
        return op === "in" ? dans : !dans;
      }
      if (op === "==" || op === "!=") {
        var eg = (estNombre(a) && estNombre(b)) ? nombre(a) === nombre(b) : (a.t === b.t && a.v === b.v) || (a.t === "none" && b.t === "none");
        return op === "==" ? eg : !eg;
      }
      var x, y;
      if (estNombre(a) && estNombre(b)) { x = nombre(a); y = nombre(b); }
      else if (a.t === "str" && b.t === "str") { x = a.v; y = b.v; }
      else throw new Erreur("TypeError", n, "'" + op + "' not supported between instances of '" + nomType(a) + "' and '" + nomType(b) + "'",
        a.t === "str" || b.t === "str" ? "on compare un texte à un nombre : une mesure lue au clavier se transforme d'abord avec float(…)." : "");
      switch (op) { case ">": return x > y; case "<": return x < y; case ">=": return x >= y; case "<=": return x <= y; }
      return false;
    },
    /* le détail d'un test pour la trace : « 118 > 118 » */
    detailTest: function (x, n) {
      var self = this;
      function val(t) { try { return texteTrace(self.eval(t, n)); } catch (e) { return "?"; } }
      if (x.k === "par") return this.detailTest(x.x, n);
      if (x.k === "cmp") {
        var s = val(x.termes[0]);
        for (var i = 0; i < x.ops.length; i++) s += " " + x.ops[i] + " " + val(x.termes[i + 1]);
        return s;
      }
      if (x.k === "nom") return x.nom + " vaut " + val(x);
      if (x.k === "et" || x.k === "ou") return this.detailTest(x.g, n) + (x.k === "et" ? " et " : " ou ") + this.detailTest(x.d, n);
      if (x.k === "non") return "non (" + this.detailTest(x.x, n) + ")";
      return val(x);
    },
    executer: function (corps) {
      for (var i = 0; i < corps.length; i++) {
        var s = corps[i];
        if (s.k === "pass") { this.note({ t: "pass", n: s.n }); continue; }
        if (s.k === "affecte") {
          var v = this.eval(s.x, s.n);
          if (s.op !== "=") {
            if (!(s.nom in this.vars)) throw new Erreur("NameError", s.n, "name '" + s.nom + "' is not defined", "« " + s.nom + " " + s.op + " … » modifie une variable qui doit déjà exister.");
            v = this.binaire(s.op[0], this.vars[s.nom], v, s.n);
          }
          this.vars[s.nom] = v;
          this.note({ t: "affecte", n: s.n, nom: s.nom, valeur: repr(v) });
          continue;
        }
        if (s.k === "expr") { this.eval(s.x, s.n); continue; }
        if (s.k === "si") {
          var pris = false;
          for (var b = 0; b < s.branches.length && !pris; b++) {
            var br = s.branches[b];
            if (br.k === "else") { this.note({ t: "sinon", n: br.n }); this.executer(br.corps); pris = true; break; }
            var detail = this.detailTest(br.test, br.n);
            var ok = vrai(this.eval(br.test, br.n));
            this.note({ t: "test", n: br.n, mot: br.k, source: br.src, detail: detail, valeur: ok });
            if (ok) { this.executer(br.corps); pris = true; }
          }
          if (!pris) this.note({ t: "aucune", n: s.branches[s.branches.length - 1].n });
        }
      }
    }
  };
  function texteTrace(v) { return v.t === "str" ? repr(v) : texte(v); }

  /* L'API : analyser (sans exécuter) et exécuter. */
  function analyser(code) {
    try { return { ok: true, programme: construire(lignesLogiques(code)) }; }
    catch (e) { if (e instanceof Erreur) return { ok: false, erreur: e }; throw e; }
  }
  function executer(code, options) {
    var a = analyser(code), m = new Machine(options);
    if (!a.ok) return { ok: false, erreur: a.erreur, trace: [], sorties: m.sorties, variables: {} };
    try { m.executer(a.programme); }
    catch (e) {
      if (!(e instanceof Erreur)) throw e;
      return { ok: false, erreur: e, trace: m.trace, sorties: m.sorties, variables: valeurs(m.vars) };
    }
    return { ok: true, trace: m.trace, sorties: m.sorties, variables: valeurs(m.vars) };
  }
  function valeurs(vars) {
    var o = {};
    Object.keys(vars).forEach(function (k) { var v = vars[k]; o[k] = v.t === "none" ? null : v.v; o["__type_" + k] = v.t; });
    return o;
  }
  /* Une phrase pour l'élève : « Ligne 17 · IndentationError — … » */
  function phraseErreur(e) {
    if (!e) return "";
    /* une limite du banc n'est jamais présentée comme une erreur de l'élève (n°340 : la simplification dite ; n°146) */
    if (e.type === "NonPrisEnCharge") return "Ligne " + e.ligne + " · limite du banc, pas forcément une erreur de ton programme — " + (e.conseil || "le banc de la page ne sait pas encore lire " + e.message + ".");
    return "Ligne " + e.ligne + " · " + e.type + " : " + e.message + (e.conseil ? " — " + e.conseil : "");
  }
  /* Une ligne de trace lisible : « ligne 12 · vent_kmh > SEUIL_OURAGAN → 118 > 118 → faux » */
  function phraseTrace(p) {
    if (p.t === "test") return "ligne " + p.n + " · " + p.mot + " " + p.source + " → " + p.detail + " → " + (p.valeur ? "vrai : on entre dans cette branche" : "faux : on passe à la suite");
    if (p.t === "sinon") return "ligne " + p.n + " · else : aucun test n'était vrai, on entre dans le sinon";
    if (p.t === "aucune") return "aucun test vrai : aucune de ces branches ne s'exécute, les valeurs de départ restent";
    if (p.t === "affecte") return "ligne " + p.n + " · " + p.nom + " reçoit " + p.valeur;
    if (p.t === "appel") return "ligne " + p.n + " · appel de " + p.nom + "(" + p.args.join(", ") + ")";
    if (p.t === "pass") return "ligne " + p.n + " · pass : rien à faire";
    return "";
  }
  /* Une empreinte courte du programme : un essai se rattache à la version qu'il a essayée (règle d'or n°333 : un code modifié après le test est « à retester »). */
  function empreinte(code) {
    var s = String(code).replace(/\r\n?/g, "\n"), h = 0x811c9dc5;
    for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 0x01000193) >>> 0; }
    return ("0000000" + h.toString(16)).slice(-8);
  }

  global.BancPython = { analyser: analyser, executer: executer, phraseErreur: phraseErreur, phraseTrace: phraseTrace, empreinte: empreinte, Erreur: Erreur, version: "1.1" };
})(typeof window !== "undefined" ? window : globalThis);
