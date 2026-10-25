/* Lecteur pas à pas commun (règles d'or n°119 et n°305). Source unique : _outils/lecteur_pas_a_pas/lecteur.js,
   posé dans chaque page par _outils/lecteur_pas_a_pas/poser.py — ne pas le modifier dans une page.
   La page garde son dessin et ses scènes ; le lecteur fait le reste : étapes, chapitres, voix, déroulé,
   mouvement réduit, impression, lien direct. Rien ne démarre ni ne parle sans un geste de l'élève. */
(function(){
  "use strict";
  if (window.LecteurPasAPas) return;
  var calme = window.matchMedia ? window.matchMedia("(prefers-reduced-motion: reduce)") : {matches: false};
  var lecteurs = [];                                     // un seul lecteur de la page parle à la fois

  function LecteurPasAPas(bloc, o){
    if (!bloc) return null;
    o = o || {};
    bloc.setAttribute("data-lpp-racine", "");
    if (o.voix) bloc.setAttribute("data-lpp-voix", o.voix);     // lu par le banc : chaque étape a son fichier
    var S = o.scenes || [], N = S.length, scene = 1, tScene = 0, MOT = o.mot || "Étape";
    function q(nom){ return bloc.querySelector('[data-lpp="' + nom + '"]'); }
    var dessin = q("dessin"), titre = q("titre"), texte = q("texte"), compte = q("compte");
    var prec = q("prec"), suiv = q("suiv"), zero = q("zero");
    var bRegarder = q("regarder"), bEcouter = q("ecouter"), sansVoix = q("sansvoix");
    var bOuvrir = q("ouvrir"), panneau = q("panneau");
    var chapitres = [].slice.call(bloc.querySelectorAll("[data-aller]"));
    var moi = {};

    // ── L'impression : la liste des étapes (rien n'est porté par le seul mouvement) ──
    if (o.imprimer !== false) {
      var liste = document.createElement("ol");
      liste.className = "lpp-imprime";
      S.forEach(function(s){
        var li = document.createElement("li");
        li.innerHTML = (s.t ? "<b>" + s.t + "</b> — " : "") + s.p;
        liste.appendChild(li);
      });
      bloc.appendChild(liste);
    } else bloc.classList.add("lpp-sans-impression");

    // ── La boucle : elle ne tourne que si le bloc est à l'écran, l'onglet visible, et le mouvement permis ──
    var raf = 0, avantT = 0, visible = true;
    function ouvert(){ return !panneau || !panneau.hidden; }
    function doitTourner(){
      if (!o.maj || !visible || document.hidden || !ouvert()) return false;
      return !calme.matches || !!(o.tourne && o.tourne(scene));
    }
    function boucle(ts){
      raf = 0;
      if (!doitTourner()) { avantT = 0; return; }
      var dt = avantT ? Math.min(.05, (ts - avantT) / 1000) : 0;
      avantT = ts; tScene += dt; o.maj(dt, scene, tScene);
      raf = requestAnimationFrame(boucle);
    }
    function relancer(){ if (!raf && doitTourner()) { avantT = 0; raf = requestAnimationFrame(boucle); } }
    function imageFixe(){ if (o.fixe) o.fixe(scene); else if (o.maj) o.maj(0, scene, tScene); }
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function(e){ visible = e[e.length - 1].isIntersecting; relancer(); }).observe(bloc);
    }
    document.addEventListener("visibilitychange", relancer);
    if (calme.addEventListener) calme.addEventListener("change", function(){ if (calme.matches) imageFixe(); relancer(); });

    // ── Changer d'étape ──
    // auto : l'étape vient du déroulé (« Regarder »), pas d'un clic de l'élève.
    function montrer(n, auto){
      var cible = Math.max(1, Math.min(N, n)), ancienne = scene;
      if (o.avant && cible > ancienne && o.avant(ancienne, cible, !!auto) === false) return false;   // étape à mériter
      scene = cible; tScene = 0;
      bloc.setAttribute("data-scene", String(scene));
      // data-de / data-a : de l'étape n à l'étape m ; data-des et data-seul : les noms écrits par les générateurs
      // des premières animations (vélo-cargo), lus tels quels.
      bloc.querySelectorAll("[data-de],[data-a],[data-des],[data-seul]").forEach(function(el){
        var de = +(el.getAttribute("data-de") || el.getAttribute("data-des") || el.getAttribute("data-seul") || 1);
        var a = +(el.getAttribute("data-a") || el.getAttribute("data-seul") || N);
        el.classList.toggle("lpp-cache", scene < de || scene > a);
      });
      var s = S[scene - 1] || {};
      if (dessin && s.d) dessin.setAttribute("aria-label", s.d);
      if (titre) titre.textContent = MOT + " " + scene + (s.t ? " — " + s.t : "");
      if (texte) texte.innerHTML = "<p>" + (s.p || "") + "</p>";
      if (compte) compte.textContent = MOT + " " + scene + " / " + N;
      if (prec) prec.disabled = scene === 1;
      if (suiv) suiv.disabled = scene === N;
      var courant = null;
      chapitres.forEach(function(b){ if (+b.getAttribute("data-aller") <= scene) courant = b; });
      chapitres.forEach(function(b){ if (b === courant) b.setAttribute("aria-current", "step"); else b.removeAttribute("aria-current"); });
      if (o.entrer) o.entrer(scene, ancienne, !!auto);
      if (calme.matches) imageFixe(); else if (o.maj) o.maj(0, scene, tScene);
      relancer();
      return true;
    }

    // ── La voix : les fichiers de la séance (synthèse neuronale hors ligne, jamais le réseau) ; en secours, ──
    // ── une voix française LOCALE du système (jamais une voix en ligne). ──
    var regarde = false, minuterie = null, jeton = 0, lecteur = null, ext = "";
    if (o.voix) {
      lecteur = new Audio();
      try { ext = lecteur.canPlayType('audio/ogg; codecs="opus"') ? "ogg" : (lecteur.canPlayType("audio/mpeg") ? "mp3" : ""); }
      catch (e) { ext = ""; }
    }
    var son = !!ext, synth = (bEcouter || bRegarder) ? (window.speechSynthesis || null) : null, voix = null;
    function choisirVoix(){
      var fr = (synth ? synth.getVoices() : []).filter(function(v){ return /^fr/i.test(v.lang) && v.localService; });
      voix = fr.filter(function(v){ return /^fr-FR/i.test(v.lang); })[0] || fr[0] || null;
      if (bEcouter) bEcouter.hidden = !(son || voix);
      if (sansVoix) sansVoix.hidden = !!(son || voix);
    }
    if (synth && "onvoiceschanged" in synth) synth.addEventListener("voiceschanged", choisirVoix);
    function brut(i){ var d = document.createElement("div"); d.innerHTML = S[i - 1].p; return d.textContent; }
    function duree(i){ return Math.max(3500, brut(i).split(/\s+/).length * (o.msParMot || 400)) + 1000; }
    function parlerSynth(i, finir){
      var j = ++jeton;
      if (!voix) { if (finir) minuterie = setTimeout(function(){ if (j === jeton) finir(); }, duree(i)); return; }
      synth.cancel();
      var u = new SpeechSynthesisUtterance(brut(i)), fait = false, secours;
      u.voice = voix; u.lang = voix.lang; u.rate = .95;
      function f(){ if (fait || j !== jeton) return; fait = true; clearTimeout(secours); if (finir) finir(); }
      u.onend = f; u.onerror = f;
      secours = setTimeout(f, duree(i) * 2 + 2000);
      synth.speak(u);
    }
    function parler(i, finir){
      lecteurs.forEach(function(l){ if (l !== moi) l.arreter(); });
      if (!son) { parlerSynth(i, finir); return; }
      var j = ++jeton, fait = false, secours;
      if (synth) synth.cancel();
      function f(){ if (fait || j !== jeton) return; fait = true; clearTimeout(secours); if (finir) finir(); }
      function bascule(){
        if (fait || j !== jeton) return;
        fait = true; clearTimeout(secours); lecteur.pause();
        if (!voix) { if (bEcouter) bEcouter.hidden = true; if (sansVoix) sansVoix.hidden = false; }
        parlerSynth(i, finir);
      }
      lecteur.onended = f; lecteur.onerror = bascule;
      secours = setTimeout(f, duree(i) * 2 + 2000);
      lecteur.src = o.voix + i + "." + ext;
      var essai = lecteur.play();
      if (essai && essai.catch) essai.catch(bascule);
    }
    function arreter(){
      regarde = false; jeton++; clearTimeout(minuterie);
      if (lecteur) lecteur.pause();
      if (synth) synth.cancel();
      if (bRegarder) bRegarder.textContent = "▶ Regarder";
    }
    function derouler(){
      if (!regarde) return;
      parler(scene, function(){
        minuterie = setTimeout(function(){
          if (!regarde) return;
          if (scene < N && montrer(scene + 1, true)) derouler(); else arreter();
        }, 1200);
      });
    }
    function demarrer(){
      if (scene === N) montrer(1);
      regarde = true; if (bRegarder) bRegarder.textContent = "⏸ Pause"; derouler();
    }
    if (prec) prec.addEventListener("click", function(){ arreter(); montrer(scene - 1); });
    if (suiv) suiv.addEventListener("click", function(){ arreter(); montrer(scene + 1); });
    if (zero) zero.addEventListener("click", function(){ arreter(); montrer(1); if (suiv) suiv.focus(); });
    if (bRegarder) bRegarder.addEventListener("click", function(){ if (regarde) arreter(); else demarrer(); });
    if (bEcouter) bEcouter.addEventListener("click", function(){ arreter(); parler(scene); });
    chapitres.forEach(function(b){ b.addEventListener("click", function(){ arreter(); montrer(+b.getAttribute("data-aller")); }); });
    if (bOuvrir && panneau) bOuvrir.addEventListener("click", function(){
      var ouvrir = panneau.hidden;
      panneau.hidden = !ouvrir;
      bOuvrir.setAttribute("aria-expanded", String(ouvrir));
      if (o.ouvrir) o.ouvrir(ouvrir);
      if (!ouvrir) arreter();
      relancer();
    });
    document.addEventListener("click", function(e){ if (e.target.closest && e.target.closest("[role=tab]")) arreter(); });
    document.addEventListener("visibilitychange", function(){ if (document.hidden) arreter(); });
    window.addEventListener("pagehide", arreter);

    // ── Impression : l'étape choisie (la dernière par défaut) le temps d'imprimer ──
    var avantImpression = null;
    window.addEventListener("beforeprint", function(){
      if (o.imprimer === false) return;
      arreter(); avantImpression = scene;
      montrer(typeof o.imprimer === "number" ? o.imprimer : N); imageFixe();
    });
    window.addEventListener("afterprint", function(){
      if (avantImpression !== null) { montrer(avantImpression); avantImpression = null; }
    });

    // ── Lien direct (cahier de textes) : #id du bloc ouvre la séance qui le porte, puis le bloc ──
    function allerAuLien(){
      if (!bloc.id || location.hash !== "#" + bloc.id) return;
      var onglet = o.onglet ? document.getElementById(o.onglet) : null;
      if (onglet && !onglet.classList.contains("active")) onglet.click();
      if (bOuvrir && panneau && panneau.hidden) bOuvrir.click();
      setTimeout(function(){ bloc.scrollIntoView({block: "start"}); }, 450);
    }
    window.addEventListener("hashchange", allerAuLien);
    if (document.readyState === "complete") allerAuLien();
    else window.addEventListener("load", allerAuLien);

    moi.montrer = montrer;
    moi.arreter = arreter;
    moi.regarder = function(){ if (!regarde) demarrer(); };
    moi.relancer = relancer;
    moi.scene = function(){ return scene; };
    moi.calme = function(){ return calme.matches; };
    lecteurs.push(moi);
    choisirVoix();
    montrer(o.depart || 1);
    return moi;
  }
  window.LecteurPasAPas = LecteurPasAPas;
})();
