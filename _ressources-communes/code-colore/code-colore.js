/* code-colore.js — le code coloré façon IDE (règle d'or n°13), pour tout le site (05/11/2026).
 *
 * Pascal, le 30/07/2026 : « J'aimerais avoir des couleurs pour les variables, constantes…, comme un IDE, par exemple
 * Sublime Text ou PyCharm. » Puis le 05/11/2026, sur le lampadaire de 4e_C9.1 : « sa zone de code est monochrome. À
 * l'avenir, il faudrait changer ceci. De façon à avoir des couleurs. »
 *
 * La palette est celle de la règle n°13 (_outils/METHODE.md) : variables cyan, chaînes vertes, nombres orange,
 * mots-clés violets en gras, « = » et opérateurs jaunes en gras, commentaires gris bleu en italique.
 * Trois langages : "python", "arduino" (le C des cartes) et "algo" (le pseudo-code en français : SI … ALORS, ←).
 *
 * Usage :
 *   <link rel="stylesheet" href="…/_ressources-communes/code-colore/code-colore.css">     (dans <head>)
 *   <pre data-code-colore="python">…</pre>        (ou "arduino", ou "algo")
 *   <script src="…/_ressources-communes/code-colore/code-colore.js"></script>           (avant editeur-python.js)
 * Au chargement, chaque élément [data-code-colore] est coloré. Seul le TEXTE est découpé : les éléments déjà
 * présents (un <select>, un <b>, un trou à compléter) restent en place. Une légende 🎨 suit le premier listing de la
 * page, s'il n'y en a pas déjà une (.py-legende).
 * API : window.CodeColore.html(texte, langage) rend le HTML coloré d'un texte (l'éditeur Python s'en sert) ;
 *       window.CodeColore.colorer(element, langage) colore un élément ; window.CodeColore.legende(element, langage).
 * Sans JavaScript, le code reste lisible, en une couleur.
 */
(function () {
  "use strict";
  if (window.CodeColore) return;

  var MOTS = {
    python: /^(False|None|True|and|as|assert|break|class|continue|def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield|print|input|int|float|str|bool|range|len|round|abs|min|max|list)$/,
    arduino: /^(void|int|long|unsigned|float|double|bool|boolean|char|byte|const|if|else|while|for|do|return|break|continue|switch|case|default|true|false|HIGH|LOW|INPUT|OUTPUT|INPUT_PULLUP|setup|loop|pinMode|digitalWrite|digitalRead|analogRead|analogWrite|delay|millis|map|constrain|tone|noTone|Serial|String|define|include)$/,
    algo: /^(DÉBUT|DEBUT|FIN|SI|ALORS|SINON|TANT|QUE|FAIRE|POUR|DE|À|JUSQU|RÉPÉTER|REPETER|FOIS|ET|OU|NON|Afficher|AFFICHER|Lire|LIRE|Allumer|Éteindre|Attendre|Mesurer|vrai|faux|VRAI|FAUX|DÉMARRER|ARRÊTER|ATTENDRE|NE|RIEN|CHANGER|GARDER)$/
  };
  // dans un algorithme écrit en français, les petits mots de la phrase restent en clair (« ARRÊTER la pompe »)
  var MOTS_FRANCAIS = /^(la|le|les|l|du|des|un|une|en|au|aux|d|s|et|ou|par|sur|dans|avec|état|est)$/;
  // les identifiants : lettres accentuées comprises (un nom d'algorithme en français, une constante)
  var ID = "[A-Za-z_\\u00C0-\\u017F][A-Za-z0-9_\\u00C0-\\u017F]*";
  var MOTIF = {
    python: new RegExp('"(?:[^"\\\\\\n]|\\\\.)*"?|\'(?:[^\'\\\\\\n]|\\\\.)*\'?|#[^\\n]*|\\d+(?:[.,]\\d+)?|' + ID + "|\\s+|[\\s\\S]", "g"),
    arduino: new RegExp('"(?:[^"\\\\\\n]|\\\\.)*"?|\'(?:[^\'\\\\\\n]|\\\\.)*\'?|//[^\\n]*|/\\*[\\s\\S]*?(?:\\*/|$)|#\\s*' + ID + "|\\d+(?:\\.\\d+)?|" + ID + "|\\s+|[\\s\\S]", "g"),
    algo: new RegExp('"[^"\\n]*"?|«[^»\\n]*»?|//[^\\n]*|#[^\\n]*|\\d+(?:[.,]\\d+)?|' + ID + "|\\s+|[\\s\\S]", "g")
  };
  var OP = /^[=+\-*\/<>%!&|←≤≥≠×÷]$/;

  function classe(t, lang) {
    var c = t.charAt(0);
    if (c === '"' || c === "'" || c === "«") return "py-str";
    if (c === "#" && lang !== "arduino") return "py-com";
    if (lang === "arduino" && (t.slice(0, 2) === "//" || t.slice(0, 2) === "/*")) return "py-com";
    if (lang === "arduino" && c === "#") return "py-kw";
    if (lang === "algo" && t.slice(0, 2) === "//") return "py-com";
    if (/^\d/.test(t)) return "py-num";
    if (/^[A-Za-z_À-ſ]/.test(t)) {
      if (MOTS[lang].test(t)) return "py-kw";
      return lang === "algo" && MOTS_FRANCAIS.test(t) ? "" : "py-var";
    }
    if (OP.test(t)) return "py-op";
    return "";
  }
  function morceaux(texte, lang) {
    var re = MOTIF[lang] || MOTIF.python, m, out = [];
    re.lastIndex = 0;
    while ((m = re.exec(texte))) {
      if (!m[0]) { re.lastIndex++; continue; }
      out.push([m[0], classe(m[0], lang)]);
    }
    return out;
  }
  function echapper(t) { return t.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }
  function html(texte, lang) {
    lang = MOTIF[lang] ? lang : "python";
    return morceaux(String(texte), lang).map(function (p) {
      return p[1] ? '<span class="' + p[1] + '">' + echapper(p[0]) + "</span>" : echapper(p[0]);
    }).join("");
  }
  // colorer un élément : on ne découpe que ses nœuds texte (un <select> ou un trou à compléter reste en place)
  function colorer(el, lang) {
    lang = lang || el.getAttribute("data-code-colore") || "python";
    if (!MOTIF[lang]) lang = "python";
    if (el.getAttribute("data-code-colore-fait") === "1") return;
    var textes = [], w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        for (var p = n.parentNode; p && p !== el; p = p.parentNode) {
          if (/^(SELECT|OPTION|TEXTAREA|INPUT|BUTTON|SCRIPT|STYLE)$/.test(p.tagName)) return NodeFilter.FILTER_REJECT;
          if (p.classList && /\bpy-(var|str|num|kw|op|com)\b/.test(p.className)) return NodeFilter.FILTER_REJECT;
        }
        return n.nodeValue ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
      }
    });
    while (w.nextNode()) textes.push(w.currentNode);
    textes.forEach(function (n) {
      var f = document.createDocumentFragment();
      morceaux(n.nodeValue, lang).forEach(function (p) {
        if (!p[1]) { f.appendChild(document.createTextNode(p[0])); return; }
        var s = document.createElement("span"); s.className = p[1]; s.textContent = p[0]; f.appendChild(s);
      });
      n.parentNode.replaceChild(f, n);
    });
    el.setAttribute("data-code-colore-fait", "1");
    el.classList.add("code-colore");
  }
  function legende(apres, lang) {
    if (document.querySelector(".py-legende")) return null;
    var p = document.createElement("p");
    p.className = "py-legende";
    p.innerHTML = lang === "algo"
      ? '🎨 Lis l\'algorithme en couleurs : <span class="py-kw">MOTS-CLÉS</span> · <span class="py-var">variables</span> · <span class="py-num">nombres</span> · <span class="py-str">« textes »</span> · <span class="py-op">←</span> et opérateurs'
      : '🎨 Lis le code en couleurs : <span class="py-var">variables</span> · <span class="py-str">"textes"</span> · <span class="py-num">nombres</span> · <span class="py-kw">mots-clés</span> · <span class="py-op">=</span> et opérateurs · <span class="py-com">' + (lang === "arduino" ? "// commentaires" : "# commentaires") + "</span>";
    apres.parentNode.insertBefore(p, apres.nextSibling);
    return p;
  }
  function appliquer(racine) {
    var els = (racine || document).querySelectorAll("[data-code-colore]");
    Array.prototype.forEach.call(els, function (el, k) {
      colorer(el);
      if (k === 0) legende(el, el.getAttribute("data-code-colore"));
    });
  }

  window.CodeColore = { html: html, colorer: colorer, legende: legende, appliquer: appliquer };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", function () { appliquer(); });
  else appliquer();
})();
