(()=>{
  const escapeHtml=s=>s.replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
  function highlightPython(code){
    let out=escapeHtml(code);
    out=out.replace(/(&quot;|&#39;)(.*?)(\1)/g,'<span class="tok-string">$1$2$3</span>');
    out=out.replace(/(^|\s)(#.*)$/gm,'$1<span class="tok-comment">$2</span>');
    out=out.replace(/\b(def|class|if|else|elif|for|while|in|and|or|not|return|import|from|as|True|False|None|try|except|with|lambda)\b/g,'<span class="tok-keyword">$1</span>');
    out=out.replace(/\b(print|len|range|str|int|float|list|dict|set|input)\b/g,'<span class="tok-builtin">$1</span>');
    out=out.replace(/\b(\d+(?:\.\d+)?)\b/g,'<span class="tok-number">$1</span>');
    out=out.replace(/\b([A-Za-z_]\w*)(?=\s*\()/g,'<span class="tok-fn">$1</span>');
    return out+'\n';
  }
  function init(root,index){
    const source=root.querySelector('.codelab-source');
    if(!source)return;
    const initial=source.value.replace(/^\n/,'').replace(/\s+$/,'');
    const key=root.dataset.storageKey||`codelab:${location.pathname}:${index}`;
    const lang=root.dataset.language||'python';
    root.innerHTML=`<div class="codelab-toolbar"><span class="codelab-language">CodeLab Techno · ${lang}</span><button type="button" data-act="copy">Copier</button><button type="button" data-act="reset">Réinitialiser</button><button type="button" data-act="smaller">A−</button><button type="button" data-act="larger">A+</button><button type="button" data-act="wrap">Retour ligne</button><button type="button" data-act="download">Exporter .py</button><button type="button" data-act="full">Plein écran</button><span class="codelab-status" aria-live="polite">Prêt</span></div><div class="codelab-shell"><pre class="codelab-lines" aria-hidden="true"></pre><div class="codelab-codearea"><pre class="codelab-highlight" aria-hidden="true"></pre><textarea class="codelab-editor" aria-label="Éditeur de programme Python" spellcheck="false"></textarea></div></div>`;
    const editor=root.querySelector('.codelab-editor'), hi=root.querySelector('.codelab-highlight'), lines=root.querySelector('.codelab-lines'), status=root.querySelector('.codelab-status');
    editor.value=localStorage.getItem(key)??initial;
    let font=14, timer;
    const render=()=>{hi.innerHTML=highlightPython(editor.value);lines.textContent=Array.from({length:Math.max(1,editor.value.split('\n').length)},(_,i)=>i+1).join('\n');hi.scrollTop=editor.scrollTop;hi.scrollLeft=editor.scrollLeft;lines.scrollTop=editor.scrollTop};
    const save=()=>{localStorage.setItem(key,editor.value);status.textContent='Enregistré sur cet appareil';clearTimeout(timer);timer=setTimeout(()=>status.textContent='Sauvegarde automatique active',1800)};
    editor.addEventListener('input',()=>{render();save()});
    editor.addEventListener('scroll',render);
    editor.addEventListener('keydown',e=>{if(e.key==='Tab'){e.preventDefault();const a=editor.selectionStart,b=editor.selectionEnd;editor.setRangeText('    ',a,b,'end');render();save()}});
    root.addEventListener('click',async e=>{const b=e.target.closest('button[data-act]');if(!b)return;const a=b.dataset.act;
      if(a==='copy'){await navigator.clipboard.writeText(editor.value);status.textContent='Code copié'}
      if(a==='reset'&&confirm('Revenir au programme de départ ?')){editor.value=initial;render();save()}
      if(a==='smaller'||a==='larger'){font=Math.min(22,Math.max(11,font+(a==='larger'?1:-1)));[editor,hi,lines].forEach(x=>x.style.fontSize=font+'px')}
      if(a==='wrap')root.classList.toggle('wrap');
      if(a==='full'){root.classList.toggle('fullscreen');b.textContent=root.classList.contains('fullscreen')?'Quitter plein écran':'Plein écran'}
      if(a==='download'){const blob=new Blob([editor.value],{type:'text/x-python;charset=utf-8'}),u=URL.createObjectURL(blob),link=document.createElement('a');link.href=u;link.download=root.dataset.filename||'programme.py';link.click();URL.revokeObjectURL(u)}
    });
    render();save();
  }
  document.addEventListener('DOMContentLoaded',()=>document.querySelectorAll('.codelab-techno').forEach(init));
})();
