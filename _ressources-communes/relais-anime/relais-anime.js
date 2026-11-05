/* relais-anime.js — le relais qui claque, vu en coupe (Pascal, 05/11/2026 : « le relais claque, il faudrait vulgariser
 * ou expliquer ce terme ; il manque aussi des images réalistes ou des schémas ou une animation »).
 *
 * Anime chaque <figure class="relais-anime"> écrite par relais_figure.py : la carte envoie ou coupe l'ordre, la bobine
 * attire la lame (ou le ressort la relève), « clac », le courant passe ou non dans le circuit de la pompe.
 * Son facultatif (coupé par défaut), fabriqué dans la page : aucun fichier, aucun réseau. Sans JavaScript, la figure
 * reste le schéma au repos et son explication.
 */
(function () {
  "use strict";

  function monter(fig) {
    if (fig.classList.contains("ra-actif")) return;
    fig.classList.add("ra-actif");
    var q = function (s) { return fig.querySelector(s); };
    var commandes = q(".ra-commandes"), etat = q(".ra-etat"), clac = q(".ra-clac"), ordre = q(".ra-ordre");
    var bEnv = q(".ra-envoyer"), bCou = q(".ra-couper"), bBat = q(".ra-battre"), bSon = q(".ra-son");
    if (!commandes || !etat) return;
    commandes.hidden = false; etat.hidden = false;
    var ferme = false, clacs = 0, son = false, audio = null, battement = null;

    function bruit() {
      if (!son) return;
      try {
        audio = audio || new (window.AudioContext || window.webkitAudioContext)();
        var n = Math.floor(audio.sampleRate * 0.025), buf = audio.createBuffer(1, n, audio.sampleRate), d = buf.getChannelData(0);
        for (var i = 0; i < n; i++) d[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / n, 6);
        var src = audio.createBufferSource(), g = audio.createGain();
        g.gain.value = 0.5; src.buffer = buf; src.connect(g); g.connect(audio.destination); src.start();
      } catch (e) { /* pas de son : l'animation suffit */ }
    }
    function montrerClac() {
      if (!clac) return;
      clac.classList.remove("ra-clac-vu"); void clac.getBoundingClientRect(); clac.classList.add("ra-clac-vu");
      clacs++; bruit();
    }
    function poser(f, texte) {
      if (f === ferme) { etat.textContent = texte; return; }
      ferme = f;
      fig.classList.toggle("ra-ferme", f);
      if (ordre) ordre.textContent = f ? "ordre : 1 (envoyé)" : "ordre : 0 (coupé)";
      montrerClac();
      etat.textContent = texte + " (" + clacs + " clac" + (clacs > 1 ? "s" : "") + " jusqu'ici)";
    }
    function arreterBattement() { if (battement) { clearTimeout(battement); battement = null; bBat.disabled = false; } }

    bEnv.addEventListener("click", function () {
      arreterBattement();
      poser(true, ferme ? "L'ordre est déjà envoyé : la lame reste collée, la pompe tourne. Rien ne bouge, donc pas de clac."
                        : "Clac ! La carte envoie l'ordre : la bobine devient un aimant et attire la lame, le contact se ferme, la pompe tourne.");
    });
    bCou.addEventListener("click", function () {
      arreterBattement();
      poser(false, !ferme ? "L'ordre est déjà coupé : la lame reste levée, la pompe est arrêtée."
                          : "Clac ! La carte coupe l'ordre : la bobine n'aimante plus, le ressort relève la lame, la pompe s'arrête.");
    });
    bBat.addEventListener("click", function () {
      arreterBattement();
      bBat.disabled = true;
      var k = ferme ? 1 : 0, total = k + 12;             // six allumages, six arrêts (d'abord un arrêt si l'ordre est déjà envoyé)
      (function pas() {
        var allume = k % 2 === 0;
        poser(allume, allume ? "La pompe s'affole : allumée pour la " + (Math.floor(k / 2) + 1) + (Math.floor(k / 2) === 0 ? "re" : "e") + " fois…" : "… éteinte.");
        k++;
        if (k < total) { battement = setTimeout(pas, 650); return; }
        battement = null; bBat.disabled = false;
        etat.textContent = "Six allumages, six arrêts : douze clacs en quelques secondes. Le relais s'use à chaque clac, et l'eau arrive par à-coups. (" + clacs + " clacs jusqu'ici)";
      })();
    });
    bSon.addEventListener("click", function () {
      son = !son;
      bSon.setAttribute("aria-pressed", son ? "true" : "false");
      bSon.textContent = son ? "🔊 Son activé" : "🔇 Son coupé";
      if (son) bruit();
    });
    etat.textContent = "Au repos : l'ordre est coupé, la lame est levée par le ressort, la pompe est arrêtée.";
  }

  function monterTout() { [].forEach.call(document.querySelectorAll("figure.relais-anime"), monter); }
  window.RelaisAnime = { monter: monterTout };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", monterTout); else monterTout();
})();
