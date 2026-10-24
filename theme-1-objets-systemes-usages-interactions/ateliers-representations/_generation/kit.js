/* Ateliers des représentations — moteur commun des exercices.
   Recopié tel quel dans chaque page par le générateur : aucune bibliothèque,
   aucun réseau, aucune donnée envoyée. Les réponses de l'élève restent dans le
   navigateur (localStorage), sous une clé PAR EXERCICE : l'atelier d'une
   représentation et le cahier du niveau partagent donc le même travail. */
(function(){
  "use strict";
  /* Deux usages : une page d'atelier ou de cahier entière (données dans #donnees-page),
     ou des exercices incrustés dans une séquence (sections .atelier-incruste, chacune avec
     ses données). En mode incrusté, rien d'autre de la séquence n'est touché : ni ses
     onglets, ni ses boutons, ni sa sauvegarde. */
  function lancer(D, racine, page){

  /* ── Mémoire locale, jamais bloquante ─────────────────────────────── */
  function lire(k){ try { var v = localStorage.getItem(k); return v ? JSON.parse(v) : null; } catch(e){ return null; } }
  function ecrire(k, v){ try { localStorage.setItem(k, JSON.stringify(v)); } catch(e){} }
  function oublier(k){ try { localStorage.removeItem(k); } catch(e){} }

  function norm(s){
    return String(s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "")
      .replace(/[’`]/g, "'").replace(/œ/g, "oe").replace(/æ/g, "ae")
      .replace(/[  ]/g, " ").replace(/\s+/g, " ").trim();
  }
  function correspond(texte, motifs){
    for (var i = 0; i < motifs.length; i++){
      try { if (new RegExp(motifs[i]).test(texte)) return true; } catch(e){}
    }
    return false;
  }
  function echapper(s){
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  /* ── Valeurs des champs d'un conteneur ────────────────────────────── */
  function valeurs(boite){
    var v = {}, champs = boite.querySelectorAll("input[name], textarea[name]");
    for (var i = 0; i < champs.length; i++){
      var c = champs[i];
      if (c.closest("[data-cle]") !== boite) continue;
      if (c.type === "radio"){ if (c.checked) v[c.name] = c.value; }
      else if (c.type === "checkbox"){
        if (!v[c.name]) v[c.name] = [];
        if (c.checked) v[c.name].push(c.value);
      } else v[c.name] = c.value;
    }
    return v;
  }
  function restaurer(boite, v){
    if (!v) return;
    var champs = boite.querySelectorAll("input[name], textarea[name]");
    for (var i = 0; i < champs.length; i++){
      var c = champs[i];
      if (c.closest("[data-cle]") !== boite) continue;
      if (!(c.name in v)) continue;
      if (c.type === "radio") c.checked = (v[c.name] === c.value);
      else if (c.type === "checkbox") c.checked = (v[c.name] || []).indexOf(c.value) >= 0;
      else c.value = v[c.name];
    }
  }

  /* ── Schémas vivants : le texte choisi s'écrit dans le dessin ─────── */
  function ecrireSvg(el, chaine){
    if (!el) return;
    var car = parseInt(el.getAttribute("data-car") || "18", 10);
    var max = parseInt(el.getAttribute("data-lignes") || "3", 10);
    var vide = el.getAttribute("data-vide") || "…";
    var x = el.getAttribute("x"), interligne = parseFloat(el.getAttribute("data-interligne") || "1.15");
    var brut = String(chaine || "").trim();
    var prefixe = el.getAttribute("data-prefixe") || "";
    var mots = (brut ? (prefixe ? prefixe + " " : "") + brut : "").split(/\s+/).filter(Boolean);
    var lignes = [], cour = "";
    var source = mots.length ? mots : vide.split(/\s+/);
    for (var i = 0; i < source.length; i++){
      var essai = cour ? cour + " " + source[i] : source[i];
      if (essai.length > car && cour){ lignes.push(cour); cour = source[i]; } else cour = essai;
    }
    if (cour) lignes.push(cour);
    if (lignes.length > max){ lignes = lignes.slice(0, max); lignes[max - 1] = lignes[max - 1].replace(/.{0,2}$/, "…"); }
    while (el.firstChild) el.removeChild(el.firstChild);
    var debut = -((lignes.length - 1) / 2) * interligne;
    for (var j = 0; j < lignes.length; j++){
      var t = document.createElementNS("http://www.w3.org/2000/svg", "tspan");
      t.setAttribute("x", x);
      t.setAttribute("dy", (j === 0 ? debut : interligne) + "em");
      t.textContent = lignes[j];
      el.appendChild(t);
    }
    if (el.classList) el.classList.toggle("rempli", mots.length > 0);
  }
  function miroirs(boite){
    var liens = boite.querySelectorAll("[data-miroir]");
    for (var i = 0; i < liens.length; i++){
      var c = liens[i], cible = document.getElementById(c.getAttribute("data-miroir"));
      if (!cible) continue;
      if (c.type === "radio"){ if (c.checked) ecrireSvg(cible, c.getAttribute("data-texte") || c.value); }
      else if (c.tagName === "TEXTAREA" || c.type === "text") ecrireSvg(cible, c.value);
    }
    // Un groupe de boutons sans choix laisse la bulle vide.
    var groupes = {};
    for (var k = 0; k < liens.length; k++){
      var r = liens[k];
      if (r.type !== "radio") continue;
      groupes[r.name] = groupes[r.name] || {cible: r.getAttribute("data-miroir"), coche: false};
      if (r.checked) groupes[r.name].coche = true;
    }
    for (var n in groupes){ if (!groupes[n].coche) ecrireSvg(document.getElementById(groupes[n].cible), ""); }
  }

  /* ── Encoches ─────────────────────────────────────────────────────── */
  function encoche(boite, pour, etat, texte){
    var el = boite.querySelector('.encoche[data-pour="' + pour + '"]');
    if (!el) return;
    var sym = {juste: "✔", faux: "✘", vide: "○"}[etat] || "";
    var mot = texte || {juste: "juste", faux: "à revoir", vide: "sans réponse"}[etat] || "";
    el.className = "encoche " + etat;
    el.innerHTML = sym + '<span class="encoche-texte">' + mot + "</span>";
  }
  function effacerEncoches(boite){
    var els = boite.querySelectorAll(".encoche"), i;
    for (i = 0; i < els.length; i++){ els[i].className = "encoche"; els[i].textContent = ""; }
    var rs = boite.querySelectorAll(".retour-option");
    for (i = 0; i < rs.length; i++) rs[i].remove();
  }
  function retourOption(boite, name, valeur, texte){
    var c = boite.querySelector('input[name="' + name + '"][value="' + CSS.escape(valeur) + '"]');
    if (!c || !texte) return;
    var lab = c.closest(".option");
    var s = document.createElement("span");
    s.className = "retour-option";
    s.textContent = texte;
    lab.insertAdjacentElement("afterend", s);
  }

  /* ── Les vérificateurs, un par type de question ──────────────────── */
  var VERIF = {
    choix: function(w, v, boite){
      var r = v[w.name];
      if (!r){ encoche(boite, w.name, "vide"); return {justes: 0, total: 1, messages: [w.vide || "Choisis une réponse."]}; }
      var ok = (r === w.bonne);
      encoche(boite, w.name, ok ? "juste" : "faux");
      retourOption(boite, w.name, r, (w.retours || {})[r]);
      return {justes: ok ? 1 : 0, total: 1, messages: ok ? [] : [w.indice || "Relis la question : une seule proposition y répond vraiment."]};
    },
    cases: function(w, v, boite){
      var coches = v[w.name] || [], justes = 0, total = w.toutes.length, msgs = [];
      for (var i = 0; i < w.toutes.length; i++){
        var val = w.toutes[i], attendu = w.bonnes.indexOf(val) >= 0, coche = coches.indexOf(val) >= 0;
        var ok = (attendu === coche);
        if (ok) justes++;
        encoche(boite, w.name + "::" + i, ok ? "juste" : "faux", ok ? (coche ? "bien coché" : "bien laissé") : (coche ? "à décocher" : "à cocher"));
        if (coche) retourOption(boite, w.name, val, (w.retours || {})[val]);
      }
      if (!coches.length) msgs.push(w.vide || "Coche au moins une case.");
      else if (justes < total) msgs.push(w.indice || "Une ou plusieurs cases sont à revoir : relis chaque proposition seule.");
      return {justes: coches.length ? justes : 0, total: total, messages: msgs};
    },
    classer: function(w, v, boite){
      var justes = 0, msgs = [], vides = 0;
      for (var i = 0; i < w.items.length; i++){
        var it = w.items[i], r = v[it.name];
        if (!r){ vides++; encoche(boite, it.name, "vide"); continue; }
        var ok = (r === it.bonne);
        if (ok) justes++;
        encoche(boite, it.name, ok ? "juste" : "faux");
        if (!ok && it.indice) msgs.push(it.indice);
      }
      if (vides) msgs.unshift(vides + (vides > 1 ? " lignes n'ont" : " ligne n'a") + " pas encore de réponse.");
      return {justes: justes, total: w.items.length, messages: msgs};
    },
    liste: function(w, v, boite){
      var lignes = String(v[w.name] || "").split(/\n|;/).map(function(l){ return l.trim(); }).filter(Boolean);
      var vus = {}, bons = 0, msgs = [], refus = 0;
      function cite(l){ return "« " + l + " »"; }
      lignes.forEach(function(l){
        var n = norm(l), i;
        for (i = 0; i < (w.refuses || []).length; i++){
          if (correspond(n, w.refuses[i].motifs)){ refus++; msgs.push(w.refuses[i].message.replace("{ligne}", cite(l))); return; }
        }
        for (i = 0; i < w.attendus.length; i++){
          if (correspond(n, w.attendus[i].motifs)){
            if (vus[i]){ msgs.push(cite(l) + " : déjà dans ta liste sous un autre nom."); return; }
            vus[i] = true; bons++; return;
          }
        }
        msgs.push((w.inconnu || "{ligne} : je ne le reconnais pas. Vérifie qu'il est bien dans la situation.").replace("{ligne}", cite(l)));
      });
      var ok = bons >= w.min && refus === 0;
      encoche(boite, w.name, lignes.length ? (ok ? "juste" : "faux") : "vide",
              lignes.length ? (bons + " reconnu" + (bons > 1 ? "s" : "") + ", " + w.min + " demandé" + (w.min > 1 ? "s" : "")) : "");
      if (!lignes.length) msgs.unshift(w.vide || "Ta liste est vide : écris une ligne par élément.");
      else if (bons < w.min) msgs.unshift("Il en faut au moins " + w.min + " : tu en as " + bons + " qui conviennent.");
      var points = Math.min(bons, w.min);
      if (refus) points = Math.max(0, points - 1);
      return {justes: points, total: w.min, messages: msgs};
    },
    texte: function(w, v, boite){
      var brut = String(v[w.name] || ""), n = norm(brut), msgs = [], justes = 0, i;
      if (brut.trim().length < (w.minCar || 10)){
        encoche(boite, w.name, "vide");
        return {justes: 0, total: w.criteres.length, messages: [w.vide || "Écris ta réponse : une phrase complète suffit."]};
      }
      for (i = 0; i < (w.interdits || []).length; i++){
        if (correspond(n, w.interdits[i].motifs)) msgs.push(w.interdits[i].message);
      }
      for (i = 0; i < w.criteres.length; i++){
        var c = w.criteres[i], nb = 0;
        for (var j = 0; j < c.motifs.length; j++){ try { if (new RegExp(c.motifs[j]).test(n)) nb++; } catch(e){} }
        var ok = nb >= (c.min || 1);
        if (ok) justes++; else msgs.push(c.manque);
        encoche(boite, w.name + "::" + i, ok ? "juste" : "faux");
      }
      var pen = (w.interdits || []).some(function(x){ return correspond(n, x.motifs); }) ? 1 : 0;
      var total = w.criteres.length;
      encoche(boite, w.name, (justes === total && !pen) ? "juste" : "faux", justes + " point" + (justes > 1 ? "s" : "") + " sur " + total);
      return {justes: Math.max(0, justes - pen), total: total, messages: msgs};
    },
    slots: function(w, v, boite){
      var justes = 0, vides = 0, msgs = [], groupes = {}, i;
      for (i = 0; i < w.slots.length; i++){
        var s = w.slots[i];
        if (s.groupe){ groupes[s.groupe] = groupes[s.groupe] || []; groupes[s.groupe].push(s); }
      }
      var dejaVu = {};
      for (i = 0; i < w.slots.length; i++){
        var sl = w.slots[i], r = v[sl.name];
        if (!r){ vides++; encoche(boite, sl.name, "vide"); continue; }
        var ok;
        if (sl.groupe){
          var cle = sl.groupe + "|" + r;
          ok = sl.bonnes.indexOf(r) >= 0 && !dejaVu[cle];
          dejaVu[cle] = true;
        } else ok = sl.bonnes.indexOf(r) >= 0;
        if (ok) justes++; else if (sl.indice) msgs.push(sl.indice);
        encoche(boite, sl.name, ok ? "juste" : "faux");
      }
      if (vides) msgs.unshift(vides + (vides > 1 ? " cases du schéma sont" : " case du schéma est") + " encore vide" + (vides > 1 ? "s" : "") + ".");
      return {justes: justes, total: w.slots.length, messages: msgs};
    },
    croquis: function(w, v, boite){
      var etat = lire(w.cle + "__croquis") || {}, traits = etat.traits || 0, msgs = [];
      var desc = String(v[w.name + "_desc"] || "").trim();
      var coches = v[w.name + "_check"] || [];
      var dessine = traits >= (w.minTraits || 4) || desc.length >= 60;
      if (!dessine) msgs.push(w.vide || "Ton croquis est encore presque vide : trace au moins les grandes formes.");
      var nbCrit = w.checklist.length, justes = (dessine ? 1 : 0) + Math.min(coches.length, nbCrit);
      if (dessine && coches.length < nbCrit) msgs.push("Relis ton croquis avec la liste : " + (nbCrit - coches.length) + " point(s) ne sont pas encore cochés. Ajoute-les au dessin, puis coche.");
      encoche(boite, w.name, dessine && coches.length === nbCrit ? "juste" : (dessine ? "faux" : "vide"),
              dessine ? (coches.length + " point(s) sur " + nbCrit + " cochés") : "croquis à faire");
      return {justes: justes, total: nbCrit + 1, messages: msgs};
    }
  };

  /* ── Un exercice ──────────────────────────────────────────────────── */
  var EXOS = D.exercices || {};
  function exoEtat(id){ return lire(EXOS[id].cle) || {}; }

  function verifier(boite){
    var id = boite.getAttribute("data-exo"), def = EXOS[id];
    if (!def) return;
    effacerEncoches(boite);
    var v = valeurs(boite), justes = 0, total = 0, messages = [];
    def.widgets.forEach(function(w){
      var f = VERIF[w.type];
      if (!f) return;
      var r = f(w, v, boite);
      justes += r.justes; total += r.total;
      messages = messages.concat(r.messages || []);
    });
    var ratio = total ? justes / total : 0;
    var zone = boite.querySelector(".retour[data-retour]");
    var classe = ratio === 1 ? "ok" : (ratio >= 0.5 ? "mixte" : "err");
    var titre = ratio === 1 ? (def.bravo || "🎉 Tout est juste. Ouvre quand même la correction : elle dit pourquoi, et c'est ce qui se retient.")
              : (ratio >= 0.5 ? "🟡 C'est bien parti : " + justes + " point" + (justes > 1 ? "s" : "") + " sur " + total + ". Corrige les lignes marquées ✘, puis vérifie à nouveau."
              : "🔴 " + justes + " point" + (justes > 1 ? "s" : "") + " sur " + total + " pour l'instant. Relis la consigne, ouvre l'aide 1, puis vérifie à nouveau : on apprend en se corrigeant.");
    if (zone){
      zone.className = "retour visible " + classe;
      var html = "<b>" + echapper(titre) + "</b>";
      var uniques = messages.filter(function(m, i){ return m && messages.indexOf(m) === i; });
      if (uniques.length) html += "<ul>" + uniques.map(function(m){ return "<li>" + echapper(m) + "</li>"; }).join("") + "</ul>";
      zone.innerHTML = html;
    }
    var etat = exoEtat(id);
    etat.v = v; etat.verifie = true; etat.reussi = (ratio === 1); etat.score = [justes, total];
    ecrire(def.cle, etat);
    if (page) majProgression();
  }

  /* ── Sauvegarde de tout ce qui porte data-cle ─────────────────────── */
  function sauver(boite){
    var cle = boite.getAttribute("data-cle");
    if (boite.hasAttribute("data-exo")){
      var etat = lire(cle) || {};
      etat.v = valeurs(boite);
      ecrire(cle, etat);
    } else ecrire(cle, {v: valeurs(boite)});
    miroirs(boite);
    var note = document.getElementById("noteSauvegarde");
    if (note) note.textContent = "✔ Enregistré dans ce navigateur à " + new Date().toLocaleTimeString("fr-FR", {hour: "2-digit", minute: "2-digit"});
  }

  function majProgression(){
    var ids = Object.keys(EXOS), faits = 0;
    ids.forEach(function(id){
      var e = exoEtat(id), b = document.getElementById("onglet-etat-" + id);
      if (e.reussi) faits++;
      if (b) b.textContent = e.reussi ? "✔ réussi" : (e.verifie ? "◐ à reprendre" : (e.v ? "○ commencé" : "à faire"));
    });
    var barre = document.getElementById("barreProgression"), txt = document.getElementById("texteProgression");
    if (barre) barre.style.width = (ids.length ? Math.round(100 * faits / ids.length) : 0) + "%";
    if (txt) txt.textContent = faits + " exercice" + (faits > 1 ? "s" : "") + " réussi" + (faits > 1 ? "s" : "") + " sur " + ids.length;
  }

  /* ── Onglets ──────────────────────────────────────────────────────── */
  var onglets = page ? Array.prototype.slice.call(document.querySelectorAll('[role="tab"]')) : [];
  var cleOnglet = D.page + "__onglet";
  function montrer(i, focus){
    if (!onglets.length) return;
    i = Math.max(0, Math.min(onglets.length - 1, i));
    onglets.forEach(function(o, j){
      var p = document.getElementById(o.getAttribute("aria-controls"));
      o.setAttribute("aria-selected", j === i ? "true" : "false");
      o.tabIndex = (j === i) ? 0 : -1;
      if (p) p.hidden = (j !== i);
    });
    var volet = document.querySelector(".rappel-ouverture");
    if (volet){
      if (i === 0){ volet.classList.remove("volet"); volet.open = true; }
      else { volet.classList.add("volet"); volet.open = false; }
    }
    ecrire(cleOnglet, i);
    if (focus) onglets[i].focus();
  }
  onglets.forEach(function(o, i){
    o.addEventListener("click", function(){ montrer(i, false); });
    o.addEventListener("keydown", function(e){
      if (e.key === "ArrowRight"){ e.preventDefault(); montrer(i + 1, true); }
      else if (e.key === "ArrowLeft"){ e.preventDefault(); montrer(i - 1, true); }
      else if (e.key === "Home"){ e.preventDefault(); montrer(0, true); }
      else if (e.key === "End"){ e.preventDefault(); montrer(onglets.length - 1, true); }
    });
  });
  if (page) document.querySelectorAll("button.suivant[data-vers]").forEach(function(b){
    b.addEventListener("click", function(){
      montrer(parseInt(b.getAttribute("data-vers"), 10), false);
      var barre = document.querySelector(".onglets");
      if (barre) barre.scrollIntoView({block: "start"});
    });
  });

  /* ── Croquis : un vrai crayon, au doigt ou à la souris ────────────── */
  function croquis(canvas){
    var cle = canvas.getAttribute("data-cle-croquis"), ctx = canvas.getContext("2d");
    var outil = "crayon", trace = false, pile = [], etat = lire(cle) || {traits: 0};
    function fond(){ ctx.fillStyle = "#ffffff"; ctx.fillRect(0, 0, canvas.width, canvas.height); }
    fond();
    if (etat.image){ var im = new Image(); im.onload = function(){ ctx.drawImage(im, 0, 0); }; im.src = etat.image; }
    function point(e){
      var r = canvas.getBoundingClientRect();
      return {x: (e.clientX - r.left) * canvas.width / r.width, y: (e.clientY - r.top) * canvas.height / r.height};
    }
    var minuterie = null;
    function memoriser(){
      clearTimeout(minuterie);
      minuterie = setTimeout(function(){
        try { etat.image = canvas.toDataURL("image/png"); } catch(e){}
        ecrire(cle, etat);
        var note = document.getElementById("noteSauvegarde");
        if (note) note.textContent = "✔ Croquis enregistré dans ce navigateur";
      }, 500);
    }
    canvas.addEventListener("pointerdown", function(e){
      e.preventDefault();
      try { pile.push(ctx.getImageData(0, 0, canvas.width, canvas.height)); if (pile.length > 20) pile.shift(); } catch(x){}
      trace = true; canvas.setPointerCapture(e.pointerId);
      var p = point(e); ctx.beginPath(); ctx.moveTo(p.x, p.y);
      ctx.lineCap = "round"; ctx.lineJoin = "round";
      ctx.strokeStyle = outil === "gomme" ? "#ffffff" : (outil === "rouge" ? "#c0182b" : "#1b2438");
      ctx.lineWidth = outil === "gomme" ? 22 : (outil === "epais" ? 6 : 3);
    });
    canvas.addEventListener("pointermove", function(e){
      if (!trace) return;
      var p = point(e); ctx.lineTo(p.x, p.y); ctx.stroke();
    });
    function fin(){ if (!trace) return; trace = false; if (outil !== "gomme") etat.traits = (etat.traits || 0) + 1; memoriser(); }
    canvas.addEventListener("pointerup", fin);
    canvas.addEventListener("pointercancel", fin);
    var barre = canvas.parentNode.querySelector(".croquis-outils");
    if (barre){
      barre.querySelectorAll("[data-outil]").forEach(function(b){
        b.addEventListener("click", function(){
          outil = b.getAttribute("data-outil");
          barre.querySelectorAll("[data-outil]").forEach(function(x){ x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        });
      });
      var annuler = barre.querySelector("[data-action=annuler]"), tout = barre.querySelector("[data-action=effacer]");
      if (annuler) annuler.addEventListener("click", function(){
        if (pile.length){ ctx.putImageData(pile.pop(), 0, 0); etat.traits = Math.max(0, (etat.traits || 0) - 1); memoriser(); }
      });
      if (tout) tout.addEventListener("click", function(){
        if (!window.confirm("Effacer tout ton croquis ?")) return;
        pile = []; fond(); etat = {traits: 0}; memoriser();
      });
    }
  }
  racine.querySelectorAll("canvas.croquis-zone").forEach(croquis);

  /* ── Branchements ─────────────────────────────────────────────────── */
  var boites = racine.querySelectorAll("[data-cle]");
  for (var i = 0; i < boites.length; i++){
    (function(b){
      var e = lire(b.getAttribute("data-cle"));
      if (e) restaurer(b, e.v);
      miroirs(b);
      b.addEventListener("input", function(){ sauver(b); });
      b.addEventListener("change", function(){ sauver(b); });
      var bouton = b.querySelector("button.verifier");
      if (bouton && b.hasAttribute("data-exo")) bouton.addEventListener("click", function(){ verifier(b); });
    })(boites[i]);
  }

  if (!page) return;
  var btnImp = document.getElementById("btnImprimer");
  if (btnImp) btnImp.addEventListener("click", function(){ window.print(); });
  var btnEff = document.getElementById("btnEffacer");
  if (btnEff) btnEff.addEventListener("click", function(){
    if (!window.confirm("Effacer tout ce que tu as écrit sur cette page ? Le travail des mêmes exercices disparaîtra aussi de ton cahier.")) return;
    for (var j = 0; j < boites.length; j++){ oublier(boites[j].getAttribute("data-cle")); }
    document.querySelectorAll("canvas.croquis-zone").forEach(function(c){ oublier(c.getAttribute("data-cle-croquis")); });
    oublier(cleOnglet);
    location.reload();
  });
  var btnEss = document.getElementById("btnEssentiel"), cleEss = D.page + "__essentiel";
  function essentiel(on){
    document.body.classList.toggle("essentiel", on);
    if (btnEss){ btnEss.setAttribute("aria-pressed", on ? "true" : "false"); btnEss.textContent = "🎯 Mode essentiel : " + (on ? "activé" : "désactivé"); }
  }
  if (btnEss){
    essentiel(!!lire(cleEss));
    btnEss.addEventListener("click", function(){ var on = !document.body.classList.contains("essentiel"); essentiel(on); ecrire(cleEss, on); });
  }

  var depart = lire(cleOnglet);
  var ancre = (location.hash || "").replace("#", "");
  if (ancre){
    var cible = document.getElementById(ancre);
    var panneau = cible ? cible.closest('[role="tabpanel"]') : null;
    if (panneau){
      var idx = onglets.findIndex(function(o){ return o.getAttribute("aria-controls") === panneau.id; });
      if (idx >= 0) depart = idx;
    }
  }
  montrer(typeof depart === "number" ? depart : 0, false);
  if (ancre){ var c2 = document.getElementById(ancre); if (c2) setTimeout(function(){ c2.scrollIntoView({block: "start"}); }, 30); }
  window.addEventListener("hashchange", function(){
    var a = (location.hash || "").replace("#", ""), c = a ? document.getElementById(a) : null;
    var pn = c ? c.closest('[role="tabpanel"]') : null;
    if (!pn) return;
    var i = onglets.findIndex(function(o){ return o.getAttribute("aria-controls") === pn.id; });
    if (i >= 0){ montrer(i, false); setTimeout(function(){ c.scrollIntoView({block: "start"}); }, 30); }
  });
  majProgression();
  }

  var source = document.getElementById("donnees-page");
  if (source){ try { lancer(JSON.parse(source.textContent), document, true); } catch(e){} }
  var incrustes = document.querySelectorAll(".atelier-incruste");
  for (var k = 0; k < incrustes.length; k++){
    var donnees = incrustes[k].querySelector('script[type="application/json"]');
    if (!donnees) continue;
    try { lancer(JSON.parse(donnees.textContent), incrustes[k], false); } catch(e){}
  }
})();
