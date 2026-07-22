(()=>{
  const ready=fn=>document.readyState==='loading'?document.addEventListener('DOMContentLoaded',fn):fn();
  ready(()=>{
    const cards=[...document.querySelectorAll('section.card')];
    if(!cards.length)return;
    const key=`qcm:${location.pathname}`;
    let seconds=0;
    let timer=null;
    const sequenceUrl='sequence_C1.3-C1.4_SI_gestion_donnees.html';
    const panel=document.createElement('section');
    panel.className='qcm-eleve-panel';
    panel.setAttribute('aria-label','Tableau de progression du QCM');
    panel.innerHTML=`<a class="qcm-link" href="${sequenceUrl}">← Retour à la séquence</a><div class="qcm-eleve-stats"><div class="qcm-stat"><strong id="qe-answered">0</strong>Répondues</div><div class="qcm-stat"><strong id="qe-correct">0</strong>Correctes</div><div class="qcm-stat"><strong id="qe-incorrect">0</strong>Incorrectes</div><div class="qcm-stat"><strong id="qe-left">${cards.length}</strong>Restantes</div><div class="qcm-stat"><strong id="qe-time">00:00</strong>Temps</div></div><div class="qcm-progress" aria-label="Progression"><span id="qe-fill"></span></div><div class="qcm-filters"><button data-filter="all">Toutes</button><button data-filter="unanswered">Non répondues</button><button data-filter="incorrect">Incorrectes</button><button data-filter="correct">Correctes</button></div><div class="qcm-actions"><button id="qe-next">Question suivante non répondue</button><button id="qe-timer">Démarrer le minuteur</button><button id="qe-retry">Réessayer les erreurs</button><button id="qe-print">Imprimer le bilan</button><button id="qe-clear">Effacer ma progression</button></div><div class="qcm-nav" aria-label="Navigation dans les questions"></div><div id="qe-result" class="qcm-final" hidden aria-live="polite"></div>`;
    const firstFooter=document.querySelector('.footer');
    (firstFooter||cards[0]).before(panel);
    const nav=panel.querySelector('.qcm-nav');
    cards.forEach((card,index)=>{
      card.dataset.qIndex=index+1;
      const button=document.createElement('button');
      button.textContent=index+1;
      button.title=`Question ${index+1}`;
      button.addEventListener('click',()=>card.scrollIntoView({behavior:'smooth',block:'start'}));
      nav.appendChild(button);
    });
    const fmt=value=>`${String(Math.floor(value/60)).padStart(2,'0')}:${String(value%60).padStart(2,'0')}`;
    function isFilled(element){
      if(element.type==='radio'||element.type==='checkbox')return element.checked;
      return String(element.value||'').trim()!=='';
    }
    function state(card){
      const feedback=card.querySelector('.answer');
      if(feedback?.classList.contains('ok'))return'correct';
      if(feedback?.classList.contains('ko'))return'incorrect';
      return[...card.querySelectorAll('input,select,textarea')].some(isFilled)?'answered':'unanswered';
    }
    function resetCard(card){
      card.querySelectorAll('input,select,textarea').forEach(element=>{
        if(element.type==='radio'||element.type==='checkbox')element.checked=false;
        else element.value='';
      });
      const feedback=card.querySelector('.answer');
      if(feedback){
        feedback.classList.remove('ok','ko');
        feedback.textContent='';
      }
      card.querySelectorAll('.qcm-enrichment,.qcm-retry-one').forEach(element=>element.remove());
    }
    function enrich(card){
      const feedback=card.querySelector('.answer');
      if(!feedback||(!feedback.classList.contains('ok')&&!feedback.classList.contains('ko'))||feedback.querySelector('.qcm-enrichment'))return;
      const help=card.querySelector('.help')?.textContent.trim();
      const checker=card.querySelector('button[onclick*="checkMCQ"],button[onclick*="checkSelect"],button[onclick*="checkNumber"],button[onclick*="checkTextIncludes"],button[onclick*="checkMulti"]')?.getAttribute('onclick')||'';
      let detected='';
      const match=checker.match(/checkMCQ\([^,]+,\s*['"]([^'"]+)/);
      if(match){
        const input=card.querySelector(`input[value="${CSS.escape(match[1])}"]`);
        detected=input?.parentElement?.textContent.trim()||'';
      }
      const meta=(window.QCM_CORRECTIONS||{})[Number(card.dataset.qIndex)]||{};
      const correct=feedback.classList.contains('ok');
      const box=document.createElement('div');
      box.className='qcm-enrichment';
      box.innerHTML=`<p><strong>Bonne réponse :</strong> ${meta.answer||detected||'Consulte l’explication ci-dessous.'}</p><p><strong>Raisonnement :</strong> ${meta.reason||help||'La réponse s’appuie sur la notion travaillée dans la séquence.'}</p>${meta.example?`<p><strong>Exemple :</strong> ${meta.example}</p>`:''}${meta.error?`<p><strong>Erreur fréquente :</strong> ${meta.error}</p>`:''}${meta.distractors?`<p><strong>Pourquoi les autres propositions ne conviennent pas :</strong> ${meta.distractors}</p>`:''}<p class="qcm-retain"><strong>À retenir :</strong> ${meta.remember||'Relis la notion et réessaie sans cumuler de points.'}</p><p><strong>Encouragement :</strong> ${correct?'Très bien : cette notion est comprise.':'Bonne démarche : relis l’explication, puis essaie une nouvelle fois.'}</p>`;
      feedback.appendChild(box);
      if(!correct){
        const retry=document.createElement('button');
        retry.type='button';
        retry.className='qcm-retry-one';
        retry.textContent='Réessayer cette question';
        retry.addEventListener('click',()=>{
          resetCard(card);
          update();
          card.scrollIntoView({behavior:'smooth',block:'center'});
        });
        feedback.after(retry);
      }
    }
    function snapshot(){
      const data={seconds,fields:{}};
      document.querySelectorAll('input,select,textarea').forEach((element,index)=>{
        if(element.closest('.qcm-eleve-panel'))return;
        const id=element.id||`${element.name||'field'}:${index}`;
        data.fields[id]=element.type==='checkbox'||element.type==='radio'?element.checked:element.value;
      });
      localStorage.setItem(key,JSON.stringify(data));
    }
    function restore(){
      try{
        const data=JSON.parse(localStorage.getItem(key)||'{}');
        seconds=data.seconds||0;
        document.querySelectorAll('input,select,textarea').forEach((element,index)=>{
          if(element.closest('.qcm-eleve-panel'))return;
          const id=element.id||`${element.name||'field'}:${index}`;
          if(!(id in(data.fields||{})))return;
          if(element.type==='checkbox'||element.type==='radio')element.checked=!!data.fields[id];
          else element.value=data.fields[id];
        });
      }catch(error){
        console.warn('Reprise QCM impossible',error);
      }
    }
    function update(){
      let answered=0;
      let correct=0;
      let incorrect=0;
      cards.forEach((card,index)=>{
        const current=state(card);
        if(current!=='unanswered')answered++;
        if(current==='correct')correct++;
        if(current==='incorrect')incorrect++;
        nav.children[index].dataset.state=current;
        enrich(card);
      });
      const remaining=cards.length-answered;
      panel.querySelector('#qe-answered').textContent=answered;
      panel.querySelector('#qe-correct').textContent=correct;
      panel.querySelector('#qe-incorrect').textContent=incorrect;
      panel.querySelector('#qe-left').textContent=remaining;
      panel.querySelector('#qe-fill').style.width=`${Math.round(answered/cards.length*100)}%`;
      panel.querySelector('#qe-time').textContent=fmt(seconds);
      const result=panel.querySelector('#qe-result');
      if(remaining===0){
        const percent=Math.round(correct/cards.length*100);
        const mark=(correct/cards.length*20).toFixed(1).replace('.0','');
        result.hidden=false;
        result.innerHTML=`<h3>Résultat final</h3><p><strong>${correct}</strong> réponse(s) correcte(s), <strong>${incorrect}</strong> incorrecte(s), <strong>0</strong> restante — <strong>${percent}%</strong>, soit <strong>${mark}/20</strong>.</p><p><strong>Temps passé :</strong> ${fmt(seconds)}.</p><p>${percent>=80?'Excellent travail : les notions essentielles sont maîtrisées.':percent>=60?'Bon travail : révise les erreurs pour consolider les notions.':'Poursuis tes efforts : utilise les corrections détaillées puis réessaie les erreurs.'}</p>`;
      }else result.hidden=true;
      snapshot();
    }
    restore();
    setTimeout(()=>{
      cards.forEach(card=>{
        if([...card.querySelectorAll('input,select,textarea')].some(isFilled)){
          const button=card.querySelector('button[onclick*="checkMCQ"],button[onclick*="checkSelect"],button[onclick*="checkNumber"],button[onclick*="checkTextIncludes"],button[onclick*="checkMulti"]');
          if(button)button.click();
        }
      });
      update();
    },0);
    update();
    document.addEventListener('change',update);
    document.addEventListener('input',event=>{
      if(event.target.matches('input[type=text],input[type=number],textarea'))update();
    });
    new MutationObserver(update).observe(document.body,{subtree:true,attributes:true,attributeFilter:['class'],childList:true});
    panel.addEventListener('click',event=>{
      const filter=event.target.dataset.filter;
      if(filter)cards.forEach(card=>card.classList.toggle('qcm-hidden',filter!=='all'&&state(card)!==filter));
    });
    panel.querySelector('#qe-next').onclick=()=>{
      const card=cards.find(item=>state(item)==='unanswered');
      card?card.scrollIntoView({behavior:'smooth',block:'start'}):alert('Toutes les questions ont reçu une réponse.');
    };
    panel.querySelector('#qe-timer').onclick=event=>{
      if(timer){
        clearInterval(timer);
        timer=null;
        event.target.textContent='Reprendre le minuteur';
      }else{
        timer=setInterval(()=>{
          seconds++;
          update();
        },1000);
        event.target.textContent='Mettre en pause';
      }
    };
    panel.querySelector('#qe-retry').onclick=()=>{
      const errors=cards.filter(card=>state(card)==='incorrect');
      if(!errors.length){
        alert('Aucune réponse incorrecte à réessayer.');
        return;
      }
      errors.forEach(resetCard);
      update();
      errors[0].scrollIntoView({behavior:'smooth',block:'start'});
    };
    panel.querySelector('#qe-print').onclick=()=>window.print();
    panel.querySelector('#qe-clear').onclick=()=>{
      if(confirm('Effacer les réponses et la progression enregistrées sur cet appareil ?')){
        localStorage.removeItem(key);
        location.reload();
      }
    };
  });
})();
