const filters=[...document.querySelectorAll('.filter')];
const cards=[...document.querySelectorAll('.property-card')];
const priceFilter=document.querySelector('#priceFilter');
const areaFilter=document.querySelector('#areaFilter');
const empty=document.querySelector('#empty');
let activeType='all';

function updateCards(){
  let visible=0;
  cards.forEach(card=>{
    const typeOk=activeType==='all'||card.dataset.type===activeType;
    const price=Number(card.dataset.price), area=Number(card.dataset.area);
    const pv=priceFilter.value, av=areaFilter.value;
    const priceOk=pv==='all'||(pv==='10'&&price<=10)||(pv==='15'&&price>10&&price<=15)||(pv==='20'&&price>=15);
    const areaOk=av==='all'||(av==='120'&&area<=120)||(av==='180'&&area>120&&area<=180)||(av==='181'&&area>=181);
    const show=typeOk&&priceOk&&areaOk;
    card.classList.toggle('hidden',!show);
    if(show) visible++;
  });
  empty.style.display=visible?'none':'block';
}
filters.forEach(f=>f.addEventListener('click',()=>{filters.forEach(x=>x.classList.remove('active'));f.classList.add('active');activeType=f.dataset.filter;updateCards()}));
priceFilter.addEventListener('change',updateCards);
areaFilter.addEventListener('change',updateCards);

document.querySelectorAll('[data-scroll]').forEach(btn=>btn.addEventListener('click',()=>{
  const el=document.querySelector(btn.dataset.scroll); if(el) el.scrollIntoView({behavior:'smooth'});
  document.querySelector('#mobileMenu').classList.remove('open');
}));
document.querySelector('#menuBtn').addEventListener('click',()=>document.querySelector('#mobileMenu').classList.toggle('open'));

const modal=document.querySelector('#modal'), modalTitle=document.querySelector('#modalTitle');
document.querySelectorAll('.details').forEach(btn=>btn.addEventListener('click',()=>{modalTitle.textContent=btn.dataset.name;modal.classList.add('show')}));
document.querySelector('#closeModal').addEventListener('click',()=>modal.classList.remove('show'));
modal.addEventListener('click',e=>{if(e.target===modal)modal.classList.remove('show')});

document.querySelectorAll('.heart').forEach(btn=>btn.addEventListener('click',()=>{btn.textContent=btn.textContent==='♡'?'♥':'♡'}));

document.querySelector('#contactForm').addEventListener('submit',e=>{
  e.preventDefault();
  e.target.reset();
  const toast=document.querySelector('#toast');
  toast.classList.add('show');
  setTimeout(()=>toast.classList.remove('show'),3000);
});
