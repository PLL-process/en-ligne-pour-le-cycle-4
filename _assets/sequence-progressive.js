(()=>{document.addEventListener('DOMContentLoaded',()=>{
  const first=document.getElementById('conv1');
  if(first){
    const table=first.closest('table');
    const rows=[...table.querySelectorAll('tr')].filter(row=>{
      const input=row.querySelector('input[id^="conv"]');
      return input&&Number(input.id.replace('conv',''))>10;
    });
    if(rows.length){
      const note=document.createElement('p');
      note.className='progressive-note';
      note.innerHTML='<strong>Parcours essentiel :</strong> commence par les 10 premières conversions. Les 20 suivantes sont proposées en approfondissement.';
      table.before(note);
      const details=document.createElement('details');
      details.className='approfondissement';
      details.innerHTML='<summary>Approfondissement — 20 conversions supplémentaires</summary>';
      const extraTable=document.createElement('table');
      extraTable.className='info';
      rows.forEach(row=>extraTable.appendChild(row));
      details.appendChild(extraTable);
      table.after(details);
    }
  }

  const prefixesHeading=[...document.querySelectorAll('h3')].find(element=>element.textContent.includes('Associer préfixes'));
  if(prefixesHeading){
    const note=document.createElement('p');
    note.className='progressive-note';
    note.innerHTML='<strong>Repère 5e :</strong> kilo, méga, giga et téra sont essentiels pour le stockage. Milli, micro, nano et pico constituent un approfondissement scientifique.';
    prefixesHeading.after(note);
  }

  const memoryHeading=[...document.querySelectorAll('h3')].find(element=>/mémoires? volatiles?/i.test(element.textContent));
  if(memoryHeading){
    const section=memoryHeading.closest('.section')||memoryHeading.parentElement;
    const container=section?.querySelector('.drag-container');
    if(container){
      const intro=document.createElement('p');
      intro.className='progressive-note';
      intro.innerHTML='<strong>Parcours essentiel :</strong> classe d’abord la RAM, le disque dur, le SSD, la clé USB, la carte SD, la ROM, la mémoire flash et le cloud. Les mémoires internes spécialisées sont proposées ensuite.';
      memoryHeading.after(intro);

      const advancedTerms=['cache','registre','vram','sram','dram','buffer','pile','stack','tas','heap','eprom','eeprom','optique','blu-ray','cd','dvd'];
      const advancedItems=[];
      [...container.querySelectorAll('.drag-item')].forEach(item=>{
        const label=item.textContent.trim().toLowerCase();
        if(label.includes('cmos')){
          item.remove();
          return;
        }
        if(advancedTerms.some(term=>label.includes(term)))advancedItems.push(item);
      });

      if(advancedItems.length){
        const details=document.createElement('details');
        details.className='approfondissement';
        details.innerHTML='<summary>Approfondissement — mémoires internes spécialisées</summary><p>Ces éléments servent à aller plus loin. Classe-les seulement après avoir terminé le parcours essentiel.</p>';
        const advancedContainer=document.createElement('div');
        advancedContainer.className='drag-container';
        advancedItems.forEach(item=>advancedContainer.appendChild(item));
        details.appendChild(advancedContainer);
        container.after(details);
      }

      const cmos=document.createElement('div');
      cmos.className='callout';
      cmos.innerHTML='<strong>Cas particulier — mémoire CMOS :</strong> elle conserve certains paramètres grâce à une pile. Elle ne doit donc pas être classée simplement comme une mémoire qui perd toujours son contenu à l’arrêt. Ce cas est expliqué, mais retiré du classement principal pour éviter une réponse trompeuse.';
      const corrections=[...section.querySelectorAll('.answer,.corrige')];
      (corrections.at(-1)||container).after(cmos);
    }
  }
})})();
