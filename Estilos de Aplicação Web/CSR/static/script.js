function carrossel(){
      const track = document.getElementById('artistsTrack');
      let page = 0; 

      function move(dir){
        const viewport = track.parentElement.getBoundingClientRect().width;
      
        const first = track.querySelector('.artist');
        if(!first) return;
        const style = getComputedStyle(track);
        const gap = parseFloat(style.gap || '0');
        const itemWidth = first.getBoundingClientRect().width;
        const perView = Math.max(1, Math.round((viewport + gap) / (itemWidth + gap)));

        const total = track.children.length;
        const maxPage = Math.ceil(total / perView) - 1;
        page = Math.min(maxPage, Math.max(0, page + dir));
        const offset = -(viewport + gap) * page;
        track.style.transform = `translateX(${offset}px)`;
      }

      document.querySelector('[data-action="prev"]').addEventListener('click', ()=> move(-1));
      document.querySelector('[data-action="next"]').addEventListener('click', ()=> move(1));
      window.addEventListener('resize', ()=> { track.style.transform = 'translateX(0)'; page = 0; });
    }

const menuHTML = document.getElementById('menu')
const conteudoHTML = document.getElementById("conteudo")

addEventListener('DOMContentLoaded', () => {
  fetch('/api/menu')
  .then(response => response.json())
  .then(dados_menu => {
    let menu = `
      <ul class="menu" aria-label="Navegação principal">
    `
    for(const item of dados_menu){
        menu += `
        <li>
            <a href="${item.rota}">${item.nome}</a>
            <div class="dropdown" role="menu" aria-label="Submenu ${item.nome}">
              <a href="#">${item.a}</a>
              <a href="#">${item.b}</a>
              <a href="#">${item.c}</a>
              <a href="#">${item.d}</a>
            </div>
        </li>
        `
    }
    menu += `</ul>`
    menuHTML.innerHTML = menu
  })

  if(document.body.id == 'index'){
    Promise.all([
      fetch('/api/banner').then(response => response.json()),
      fetch('/api/artistas').then(response => response.json()),
      fetch('/api/destaques').then(response => response.json())
    ])
    .then(([dados_banners, dados_artistas, dados_destaques]) => {
      let pagina = `
      <section class="hero" aria-label="Em alta">
      <h1>Aplicação CSR</h1>
      <div class="hero-strip" >`

      for (item of dados_banners){
        pagina += `
          <a class="news-card" href="${item.url}" target="_blank">
            <span class="badge">${item.categoria}</span>
            <img class="thumb" src="${item.img}" alt="${item.alt}"/>
            <div class="title">${item.titulo}</div>
          </a>
        `
      }
      pagina += `</div></section>`
      pagina += `
      <section class="section" aria-labelledby="top-artistas">
      <div class="section-head">
        <h2 id="top-artistas">Top Artistas</h2>
        <div class="sub">Em alta nesta semana</div>
      </div>
      <div class="artists-wrap">
      <button class="arrow prev" aria-label="Anterior" data-action="prev">&#10094;</button>
      <div class="artists-viewport">
      <div class="artists-track" id="artistsTrack">`
      for (item of dados_artistas){
        pagina += `
        <a class="artist" href="#" aria-label="${item.nome}">
            <img src="${item.foto}" alt="${item.nome}" />
            <span class="overlay">${item.nome}</span>
        </a>
        `
      }
      pagina += `
      </div></div>
      <button class="arrow next" aria-label="Próximo" data-action="next">&#10095;</button>
      </div>
      </section>`

      pagina += `
      <section class="section" aria-label="Destaques">
      <div class="grid">`
      for(item of dados_destaques){
        pagina += `
        <article class="card">
          <img class="cover" src="${item.img}" alt="${item.alt}"/>
          <div class="body">
            <span class="chip">${item.categoria}</span>
            <h3 class="title-sm">${item.titulo}</h3>
          </div>
        </article>
        `
      }
      pagina += `
      </div>
      </section>`
      conteudoHTML.innerHTML = pagina
      carrossel()
    })
  }
  else if(document.body.id == 'noticias'){
    fetch('/api/noticias')
    .then(response => response.json())
    .then(dados_noticias => {
      let noticia = `
      <section class="section" aria-label="Destaques">
      <div class="grid">
      `

      for(item of dados_noticias){
        noticia += `
        <article class="card">
          <img class="cover" src="${item.img}" alt="" />
          <div class="body">
            <span class="chip">Notícias</span>
            <h3 class="title-sm">${item.titulo}</h3>
          </div>
        </article>  
        `
      }
      noticia += `
      </div>
      </section>
      `
      conteudoHTML.innerHTML = noticia
    })
  }
  else if(document.body.id == 'eventos'){
    fetch('/api/eventos')
    .then(response => response.json())
    .then(dados_eventos => {
      let evento = `
        <section class="section" aria-label="Destaques">
        <div class="grid">
      `
      for (item of dados_eventos){
        evento += `
          <article class="card">
             <img class="cover" src="${item.img}" alt="" />
              <div class="body">
                <span class="chip chip--pink">Eventos</span>
                <h3 class="title-sm">${item.titulo}</h3>
              </div>
          </article>
        `
      }

      evento += `
        </div>
        </section>
      `
      conteudoHTML.innerHTML = evento
    })
  }
  else if(document.body.id == 'premiacoes'){
    fetch('/api/premiacoes')
    .then(response => response.json())
    .then(dados_premiacoes => {
      let premio = `
        <section class="section" aria-label="Destaques">
        <div class="grid">
      `
      for (item of dados_premiacoes){
        premio += `
        <article class="card">
                <img class="cover" src="${item.img}" alt="" />
                <div class="body">
                    <span class="chip">Premiações</span>
                    <h3 class="title-sm">${item.titulo}</h3>
                </div>
            </article>
        `
      }

      premio += `
      </div>
      </section>
      `
      conteudoHTML.innerHTML = premio

    })
  }

})