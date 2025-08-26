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

const divConteudo = document.getElementById("conteudo")
const divMenu = document.getElementById("menu")

window.addEventListener('DOMContentLoaded', ()=>{
  fetch('/api/menu')
  .then(response => response.json())
  .then(dados_menu => {
    let menuHTML = `
      <div class="right">
        <ul class="menu" aria-label="Navegação principal">`
      
      for(let item of dados_menu){
        menuHTML += ` 
        <li>
            <a href="${item.rota}" id="${item.id}">${item.nome}</a>
            <div class="dropdown" role="menu" aria-label="Submenu Notícias">
              <a href="#">${item.a}</a>
              <a href="#">${item.b}</a>
              <a href="#">${item.c}</a>
              <a href="#">${item.d}</a>
            </div>
        </li>
        `
      }

      menuHTML += `
          </ul>
            <a href="/mudarLogin" style="text-decoration: none;">
              <button type="button" class="login-btn" aria-label="Entrar">Entrar</button>  
            </a>
            <button class="tema-btn" type="button" aria-label="Tema">Tema</button>
          </div>
        </nav>
      </header>
      `
      
      menuHTML += `
        <section class="hero" aria-label="Em alta">
        <div class="hero-strip">
      `
      divMenu.innerHTML = menuHTML
  })

  if (document.body.id == 'noticias'){
    fetch('/api/noticias')
    .then(response => response.json())
    .then(dados_noticias => {
      let noticiasHTML = "<section class='section' aria-label='Destaques'>"
      noticiasHTML += `<div class="grid">`
      for (let noticia of dados_noticias){
        noticiasHTML += `
          <article class="card">
            <img class="cover" src="${noticia.img}" alt="" />
            <div class="body">
              <span class="chip">Notícias</span>
              <h3 class="title-sm">${noticia.titulo}</h3>
            </div>
          </article>
        `
      }
      noticiasHTML += `
        </div>
        </section>
      `
      divConteudo.innerHTML = noticiasHTML
  })
  }

  else if (document.body.id == 'eventos'){
    fetch('/api/eventos')
    .then(response => response.json())
    .then(dados_eventos =>{
      let eventosHTML = `<section class="section" aria-label="Destaques">`
      eventosHTML += `<div class="grid">`

      for (const evento of dados_eventos){
        eventosHTML += `
        <article class="card">
          <img class="cover" src="${evento.img}" alt="" />
            <div class="body">
              <span class="chip chip--pink">Eventos</span>
              <h3 class="title-sm">${evento.titulo}</h3>
          </div>
        </article>
        `
      }
      eventosHTML += `
      </div>
      </section>
      `
      divConteudo.innerHTML = eventosHTML

    })
  }

  else if (document.body.id == 'premiacoes'){
    fetch("/api/premiacoes")
    .then(response => response.json())
    .then(dados_premiacoes => {
      let premiacoesHTML = `<section class="section" aria-label="Destaques">`
      premiacoesHTML += `<div class="grid">`
      for (premio of dados_premiacoes){
        premiacoesHTML += `
          <article class="card">
            <img class="cover" src="${premio.img}" alt="" />
              <div class="body">
                <span class="chip">Premiações</span>
                <h3 class="title-sm">${premio.titulo}</h3>
              </div>
          </article>`
      }
      premiacoesHTML += `
      </div>
      </section>
      `

      divConteudo.innerHTML = premiacoesHTML
    })
  }

  else if(document.body.id == 'index'){
    Promise.all([
      fetch('/api/banner').then(response => response.json()),
      fetch('/api/artistas').then(response => response.json()),
      fetch('/api/destaques').then(response => response.json())
    ]).then(([dados_banner, dados_artistas, dados_destaques]) => {

      for (const banner of dados_banner){
        indexHTML += `
          <a class="news-card" href="${banner.url}" target="_blank">
            <span class="badge">${banner.categoria}</span>
            <img class="thumb" src="${banner.img}" alt="${banner.alt}"/>
            <div class="title">${banner.titulo}</div>
          </a>
        `
      }

      indexHTML += `
        </div>
        </section>
      `

      indexHTML += `
      <section class="section" aria-labelledby="top-artistas">
        <div class="section-head">
          <h2 id="top-artistas">Top Artistas</h2>
          <div class="sub">Em alta nesta semana</div>
        </div>

        <div class="artists-wrap">
          <button class="arrow prev" aria-label="Anterior" data-action="prev">&#10094;</button>
          <div class="artists-viewport">
            <div class="artists-track" id="artistsTrack">
      `

      for (const artista of dados_artistas) {
        indexHTML += `
          <a class="artist" href="#" aria-label="${artista.nome}">
            <img src="${artista.foto}" alt="${artista.nome}" />
            <span class="overlay">${artista.nome}</span>
          </a>
        `
      }

      indexHTML += `
            </div>
          </div>
          <button class="arrow next" aria-label="Próximo" data-action="next">&#10095;</button>
        </div>
      </section>
      `

      indexHTML += `
      <section class="section" aria-label="Destaques">
        <div class="grid">
      `

      for (const destaque of dados_destaques){
        indexHTML += `
          <article class="card">
            <img class="cover" src="${destaque.img}" alt="${destaque.alt}"/>
            <div class="body">
              <span class="chip">${destaque.categoria}</span>
              <h3 class="title-sm">${destaque.titulo}</h3>
            </div>
          </article>
        `
      }

      indexHTML += `
        </div>
      </section>
      `

      divConteudo.innerHTML = indexHTML
      carrossel();
    })
}
})