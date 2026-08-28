#!/usr/bin/env node
/**
 * verificateur_ressources.mjs — les liens vidéo du dépôt sont-ils encore vivants ?
 *
 *     node verificateur_ressources.mjs           vérifie et rend compte
 *     node verificateur_ressources.mjs --maj     idem, et inscrit la date du jour
 *                                                dans « verifie_le » pour ce qui répond
 *
 * À LANCER DEPUIS TA MACHINE. Le réseau sortant du conteneur où je travaille est fermé —
 * même example.com y répond 403. Ce contrôle existe précisément parce que je ne peux pas
 * l'exécuter moi-même.
 *
 * Quatre contrôles, pas un :
 *   1. le lien répond-il ?
 *   2. pour YouTube, la vidéo existe-t-elle encore ? (une vidéo supprimée répond 200 :
 *      la page d'erreur est une page. On interroge donc oEmbed, qui, lui, répond 404.)
 *   3. chaque ressource a-t-elle son repli imprimé, et son bloc est-il encore dans sa page ?
 *      Une ressource sans repli est un défaut même quand le lien marche (règle n°169).
 *   4. la licence a-t-elle été lue à la source ? Non bloquant — un lien ne reproduit rien —
 *      mais on le rappelle tant qu'il est tôt.
 *
 * Aucune dépendance : Node 18 ou plus suffit.
 */

import { readFile, writeFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import path from "node:path";

const ICI = path.dirname(fileURLToPath(import.meta.url));
const RACINE = path.resolve(ICI, "..", "..");
const REGISTRE = path.join(ICI, "ressources_externes.json");
const MAJ = process.argv.includes("--maj");
const DELAI = 12000;

const vert = (s) => `\x1b[32m${s}\x1b[0m`;
const rouge = (s) => `\x1b[31m${s}\x1b[0m`;
const jaune = (s) => `\x1b[33m${s}\x1b[0m`;

async function joindre(url, methode = "HEAD") {
  const stop = AbortSignal.timeout(DELAI);
  try {
    const r = await fetch(url, { method: methode, redirect: "follow", signal: stop,
                                 headers: { "User-Agent": "verificateur-ressources/1.0" } });
    if (r.status === 405 && methode === "HEAD") return joindre(url, "GET");
    return { code: r.status, ok: r.ok, finale: r.url };
  } catch (e) {
    return { code: 0, ok: false, erreur: e.name === "TimeoutError" ? "délai dépassé" : e.message };
  }
}

/** Une vidéo YouTube supprimée renvoie quand même une page. oEmbed, lui, dit la vérité. */
async function youtubeVivante(url) {
  const oembed = "https://www.youtube.com/oembed?format=json&url=" + encodeURIComponent(url);
  const r = await joindre(oembed, "GET");
  if (r.code === 404) return { verdict: false, pourquoi: "la vidéo n'existe plus (oEmbed 404)" };
  if (r.code === 401 || r.code === 403) return { verdict: false, pourquoi: "vidéo privée ou restreinte" };
  if (!r.ok) return { verdict: null, pourquoi: `oEmbed injoignable (${r.code || r.erreur})` };
  return { verdict: true, pourquoi: "la vidéo répond" };
}

const estYoutube = (u) => /(^|\.)(youtube\.com|youtu\.be)$/i.test(safeHost(u));
function safeHost(u) { try { return new URL(u).hostname; } catch { return ""; } }

async function main() {
  const registre = JSON.parse(await readFile(REGISTRE, "utf8"));
  const pages = new Map();
  let morts = 0, sansRepli = 0, blocsAbsents = 0, verifies = 0, attente = 0;
  let licencesAVoir = 0;

  console.log(`\nRegistre : ${registre.ressources.length} ressource(s).\n`);

  for (const r of registre.ressources) {
    const url = (r.url || "").trim();

    // ── contrôle 3a : le repli, qu'il y ait un lien ou non ────────────────
    const repli = (r.repli && r.repli.html || "").trim();
    if (!repli) {
      console.log(`  ${rouge("✗")} ${r.id.padEnd(24)} AUCUN REPLI IMPRIMÉ — règle n°169`);
      sansRepli++;
    }

    // ── contrôle 3b : le bloc est-il encore dans sa page ? ────────────────
    if (url) {
      const chemin = path.join(RACINE, r.page);
      if (!pages.has(chemin)) {
        pages.set(chemin, await readFile(chemin, "utf8").catch(() => null));
      }
      const html = pages.get(chemin);
      if (html === null) {
        console.log(`  ${rouge("✗")} ${r.id.padEnd(24)} page introuvable : ${r.page}`);
        blocsAbsents++;
      } else if (!html.includes(`<!-- ressource: ${r.id} -->`)) {
        console.log(`  ${jaune("!")} ${r.id.padEnd(24)} bloc absent de la page — relancer poser_ressource.py`);
        blocsAbsents++;
      }
    }

    // ── contrôles 1 et 2 : le lien ────────────────────────────────────────
    if (!url) {
      console.log(`  ${jaune("⏳")} ${r.id.padEnd(24)} pas encore de vidéo`);
      attente++;
      continue;
    }

    const rep = await joindre(url);
    let ligne, vivant = rep.ok;
    if (!rep.ok) {
      ligne = rouge(`✗ ${rep.code || rep.erreur}`);
    } else if (estYoutube(url)) {
      const yt = await youtubeVivante(url);
      vivant = yt.verdict !== false;
      ligne = yt.verdict === true ? vert("✓ " + yt.pourquoi)
            : yt.verdict === false ? rouge("✗ " + yt.pourquoi)
            : jaune("? " + yt.pourquoi);
    } else {
      ligne = vert(`✓ ${rep.code}`);
    }
    console.log(`  ${ligne.padEnd(30)} ${r.id.padEnd(24)} ${safeHost(url)}`);
    if (vivant) { verifies++; if (MAJ) r.verifie_le = new Date().toISOString().slice(0, 10); }
    else morts++;

    // ── contrôle 4 : la licence a-t-elle été lue à la source ? ────────────
    // Un lien ne reproduit rien, donc rien n'est bloquant ici. Mais le jour où l'on
    // découpe, réhéberge ou intègre, la licence redevient la question — et personne
    // ne s'en souvient à ce moment-là. On le rappelle donc pendant qu'il est tôt.
    if (r.licence_verifiee !== true) {
      console.log(`     ${jaune("licence non lue à la source")}`
                + (r.verifie_comment ? ` — ${r.verifie_comment}` : ""));
      licencesAVoir++;
    }
  }

  if (MAJ) {
    await writeFile(REGISTRE, JSON.stringify(registre, null, 2) + "\n", "utf8");
    console.log(`\n  dates mises à jour dans ${path.basename(REGISTRE)}`);
  }

  console.log(`\n${verifies} lien(s) vivant(s) · ${morts} mort(s) · ${attente} en attente`
            + ` · ${sansRepli} sans repli · ${blocsAbsents} bloc(s) à reposer`
            + ` · ${licencesAVoir} licence(s) à lire\n`);
  if (morts || sansRepli) {
    console.log(rouge("Un lien mort ou une ressource sans repli, c'est une séance qui tombe.\n"));
    process.exit(1);
  }
}

main().catch((e) => { console.error(e); process.exit(2); });
