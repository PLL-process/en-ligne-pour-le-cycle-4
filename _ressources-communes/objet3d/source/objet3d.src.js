// Objet 3D manipulable (28/11/2026 ; premier usage : le vélo-cargo de 5e_C3.1). Source de ../objet3d.js : ne pas modifier
// objet3d.js à la main, relancer construire.sh. Un seul script classique (IIFE, construit par esbuild) : il marche aussi
// en file:// (clé USB, réseau du collège), où les modules ES et fetch() sont refusés par le navigateur.
import * as THREE from 'three';
import {OrbitControls} from 'three/examples/jsm/controls/OrbitControls.js';
import {GLTFLoader} from 'three/examples/jsm/loaders/GLTFLoader.js';
import {CSS2DRenderer, CSS2DObject} from 'three/examples/jsm/renderers/CSS2DRenderer.js';

function versOctets(b64) {
  const bin = atob(b64); const out = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i);
  return out.buffer;
}

function webglDispo() {
  try { const c = document.createElement('canvas'); return !!(c.getContext('webgl2') || c.getContext('webgl')); } catch (e) { return false; }
}

// boite : l'élément qui reçoit la vue ; options : {modele (base64 d'un .glb), etiquettes [{piece, numero}] (la
// pastille se pose sur l'objet vide « repere_<piece> » s'il existe),
// direction [x, y, z] : d'où l'on regarde au départ (le cadrage et la distance se calculent)}. Rend une promesse ; rejetée si WebGL manque (la page garde son image fixe).
function monter(boite, options) {
  if (!webglDispo()) return Promise.reject(new Error('WebGL indisponible'));
  const calme = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(35, 1, 0.01, 200);
  const rendu = new THREE.WebGLRenderer({antialias: true, alpha: true});
  rendu.setPixelRatio(Math.min(devicePixelRatio || 1, 2));        // au-delà de 2, un téléphone chauffe pour rien
  rendu.outputColorSpace = THREE.SRGBColorSpace;
  boite.appendChild(rendu.domElement);
  const etiq = new CSS2DRenderer();
  etiq.domElement.className = 'o3d-etiquettes';
  boite.appendChild(etiq.domElement);
  scene.add(new THREE.HemisphereLight(0xffffff, 0x223355, 2.2));
  const soleil = new THREE.DirectionalLight(0xffffff, 1.6); soleil.position.set(4, 8, 5); scene.add(soleil);
  const controles = new OrbitControls(camera, rendu.domElement);
  // cadrage : la vue tourne autour du CENTRE de l'objet ; la distance de départ fait tenir TOUS ses points dans l'image,
  // vus depuis options.direction, avec 12 % de marge pour les pastilles (la sphère englobante, puis les coins de la
  // boîte, laissaient un vélo long au milieu d'un grand vide : la moitié de la largeur). Posé après le chargement.
  const cadrer = (objet) => {
    const boite3d = new THREE.Box3().setFromObject(objet);
    const centre = boite3d.getCenter(new THREE.Vector3());
    const dir = new THREE.Vector3(...(options.direction || [1, 0.45, 1.1])).normalize();
    const aspect = (boite.clientWidth || 4) / (boite.clientHeight || 3);
    const tanV = Math.tan(THREE.MathUtils.degToRad(camera.fov) / 2) * 0.88, tanH = tanV * aspect;
    // repère de la caméra : avant = -dir, haut = Y du monde redressé, droite = avant × haut
    const avant = dir.clone().negate();
    const droite = new THREE.Vector3().crossVectors(avant, new THREE.Vector3(0, 1, 0)).normalize();
    const haut = new THREE.Vector3().crossVectors(droite, avant);
    let distance = 0; const c = new THREE.Vector3();
    objet.traverse(o => {
      if (!o.isMesh) return;
      const pos = o.geometry.attributes.position;
      for (let i = 0; i < pos.count; i++) {
        c.fromBufferAttribute(pos, i).applyMatrix4(o.matrixWorld).sub(centre);
        const prof = c.dot(dir);                     // > 0 : le point est du côté de la caméra
        distance = Math.max(distance, prof + Math.abs(c.dot(droite)) / tanH, prof + Math.abs(c.dot(haut)) / tanV);
      }
    });
    camera.position.copy(centre).addScaledVector(dir, distance);
    controles.target.copy(centre);
    controles.minDistance = distance * 0.4; controles.maxDistance = distance * 2;
    controles.update();
    controles.saveState();                     // « 0 » ou Origine y ramène
  };
  controles.enableDamping = !calme;                                 // moins de mouvement : pas d'inertie
  controles.enablePan = false;                                      // l'élève tourne et zoome, il ne perd pas l'objet
  // une pastille dont la pièce est cachée par une autre (le bac, vu de face) s'estompe : elle ne désigne plus la
  // mauvaise pièce ; quatre rayons par image, seulement quand l'élève bouge la vue
  const etiquettes = [], rayon = new THREE.Raycaster(); let modele = null;
  const appartient = (o, piece) => { for (; o; o = o.parent) if (o === piece) return true; return false; };
  const dessiner = () => {
    for (const {objet, piece} of etiquettes) {
      const vers = objet.position.clone().sub(camera.position), dist = vers.length();
      rayon.set(camera.position, vers.normalize()); rayon.far = dist;
      const t = modele ? rayon.intersectObject(modele, true)[0] : null;
      objet.element.classList.toggle('o3d-cachee', !!t && t.distance < dist - 0.03 && !appartient(t.object, piece));
    }
    rendu.render(scene, camera); etiq.render(scene, camera);
  };
  const taille = () => {
    const l = boite.clientWidth, h = boite.clientHeight;
    camera.aspect = l / h; camera.updateProjectionMatrix();
    rendu.setSize(l, h); etiq.setSize(l, h); dessiner();
  };
  new ResizeObserver(taille).observe(boite);
  // revenir à la vue de départ : l'inertie d'un glisser récent (damping) continuait de tourner après reset() ; sans
  // inertie, update() applique d'un coup ce qui restait et le remet à zéro, puis reset() pose la vue de départ
  const revenir = () => {
    const inertie = controles.enableDamping;
    controles.enableDamping = false; controles.update(); controles.reset(); controles.enableDamping = inertie;
  };
  // au clavier (la vue reçoit le focus quand elle s'ouvre) : flèches pour tourner, + et − pour zoomer, 0 pour revenir
  boite.addEventListener('keydown', e => {
    const pas = Math.PI / 12;
    const gestes = {ArrowLeft: () => controles.rotateLeft(pas), ArrowRight: () => controles.rotateLeft(-pas),
      ArrowUp: () => controles.rotateUp(pas), ArrowDown: () => controles.rotateUp(-pas),
      '+': () => controles.dollyOut(1.15), '=': () => controles.dollyOut(1.15), '-': () => controles.dollyIn(1.15),
      '0': revenir, Home: revenir};
    if (!gestes[e.key] || e.altKey || e.ctrlKey || e.metaKey) return;
    e.preventDefault(); gestes[e.key](); dessiner();
  });
  // rendu à la demande : rien ne tourne quand l'élève ne touche à rien (batterie, n°175)
  let enCours = false;
  controles.addEventListener('change', () => {
    if (enCours) return; enCours = true;
    requestAnimationFrame(() => { enCours = false; controles.update(); dessiner(); });
  });
  return new Promise((ok, ko) => {
    new GLTFLoader().parse(versOctets(options.modele), '', gltf => {
      // garde : une matière métallique sans carte d'environnement sort noire ; l'exporter non métallique (Blender :
      // Metallic = 0), et ramener ici ce qui aurait échappé
      gltf.scene.traverse(o => { if (o.isMesh && o.material && o.material.metalness > 0.5 && !o.material.metalnessMap) {
        console.warn('matière métallique ramenée à 0 :', o.name); o.material.metalness = 0; } });
      scene.add(gltf.scene); modele = gltf.scene;
      gltf.scene.updateMatrixWorld(true);
      for (const e of options.etiquettes || []) {
        const piece = gltf.scene.getObjectByName(e.piece);
        if (!piece) { console.warn('pièce absente du modèle :', e.piece); continue; }
        // l'ancre : un repère posé dans le modèle (objet vide « repere_<pièce> », choisi dans Blender sur une face que la
        // vue de départ montre) ; à défaut, le point de la pièce le plus proche du centre de sa boîte (le centre d'un
        // cadre tombe dans le vide, et son point le plus proche peut tomber sous le bac : d'où le repère)
        const ancre = new THREE.Vector3();
        const repere = gltf.scene.getObjectByName('repere_' + e.piece);
        if (repere) repere.getWorldPosition(ancre);
        else {
          const centre = new THREE.Box3().setFromObject(piece).getCenter(new THREE.Vector3());
          let mieux = Infinity; const v = new THREE.Vector3();
          piece.traverse(o => {
            if (!o.isMesh) return;
            const pos = o.geometry.attributes.position;
            for (let i = 0; i < pos.count; i += 3) {
              v.fromBufferAttribute(pos, i).applyMatrix4(o.matrixWorld);
              const d = v.distanceToSquared(centre); if (d < mieux) { mieux = d; ancre.copy(v); }
            }
          });
        }
        // la pastille se pose À CÔTÉ de la pièce (décalée en haut à droite), pas dessus : la pièce reste visible
        const porteur = document.createElement('div'); porteur.className = 'o3d-ancre';
        const pastille = document.createElement('span');
        pastille.className = 'o3d-pastille'; pastille.textContent = e.numero;
        pastille.setAttribute('aria-hidden', 'true');                // la légende est écrite dans la page
        porteur.appendChild(pastille);
        const o = new CSS2DObject(porteur); o.position.copy(ancre); scene.add(o);
        etiquettes.push({objet: o, piece});
      }
      cadrer(gltf.scene);
      taille(); ok({dessiner, controles, revenir: () => { revenir(); dessiner(); }});
    }, ko);
  });
}

window.Objet3D = {monter, webglDispo};
