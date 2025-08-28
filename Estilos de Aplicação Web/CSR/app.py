from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'chaveSuperSecreta2'

users = {'ana': '123', 'helo': '456'}

app.permanent_session_lifetime = timedelta(days=7) 

@app.route('/')
def carregarIndex():
    if 'user' in session:
        return render_template('index.html', user=session['user'], body_id = 'index')
    return redirect(url_for('paginaLogin'))  

@app.route('/mudarNoticias', methods=['GET'])
def paginaNoticias():
    if 'user' in session:
        return render_template('index.html', body_id = 'noticias')
    return redirect(url_for('paginaLogin'))  

@app.route('/mudarEventos', methods=['GET'])
def paginaEventos():
    if 'user' in session:
        return render_template('index.html', body_id = 'eventos')
    return redirect(url_for('paginaLogin'))

@app.route('/mudarPremiacoes', methods=['GET'])
def paginaPremicoes():
    if 'user' in session:
        return render_template('index.html', body_id = 'premiacoes')
    return redirect(url_for('paginaLogin'))

@app.route('/mudarLogin', methods=['GET'])
def paginaLogin():
    return render_template('login.html')

@app.route('/mudarCadastro', methods=['GET'])
def paginaCadastro():
    return render_template('cadastro.html')

@app.route('/logar', methods=['POST'])
def logar():
    username = request.form['username']
    password = request.form['password']
    remember = 'remember' in request.form  
    
    if username in users and users[username] == password:
        session['user'] = username  
        session.permanent = remember  
        
        if remember:
            app.permanent_session_lifetime = timedelta(days=7)  
        return redirect(url_for('carregarIndex'))  
    
    return render_template('login.html', mensagem='Usuário ou senha incorretos.')  

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    name = request.form['name']
    email = request.form['email']
    user = request.form['username']
    password = request.form['password']
    password2 = request.form['confirm_password']

    if not name or not email or not user or not password or not password2:
        return render_template('cadastro.html', mensagem = 'Preencha todos os campos')

    if password == password2:  
        if user not in users: 
            users[user] = password  
            return redirect(url_for('paginaLogin'))  
        else:
            return render_template('cadastro.html', mensagem='Este nome de usuário já está em uso.')  
    else:
        return render_template('cadastro.html', mensagem='As senhas não coincidem.')  

@app.route('/api/menu')
def api_menu():
    menu = [
    {'rota': '/mudarNoticias', 'id': 'linkNoticias', 'nome': 'Notícias', 'a': 'Em alta', 'b': 'Internacional', 'c': 'Nacional', 'd': 'Lançamentos'},
    {'rota': '/mudarEventos', 'id': 'linkEventos', 'nome': 'Eventos', 'a': 'Lollapalooza', 'b': 'Rock in Rio', 'c': 'Primavera Sound', 'd': 'The Town'},
    {'rota': '/mudarPremiacoes', 'id': 'linkPremiacoes', 'nome': 'Premiações', 'a': 'Grammy', 'b': 'VMA', 'c': 'Billboard Music Awards', 'd': 'MTV Miaw'},
    ]

    return jsonify(menu)

@app.route('/api/banner')
def api_banner():
    banner = [
    {'categoria': 'EM ALTA', 'alt': 'The Town', 'titulo': 'The Town garante acessibilidade e serviços para PCDs.', 'img': 'https://imgs.search.brave.com/8x7WKbELBgbM-leGrlf0yzFARw9nKFWljYckJ1LqYQc/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9mLmku/dW9sLmNvbS5ici9m/b3RvZ3JhZmlhLzIw/MjMvMDkvMTAvMTY5/NDM1MDA4NDY0ZmRi/YjA0YjExZDZfMTY5/NDM1MDA4NF8zeDJf/bWQuanBn', 'url': 'http://g1.globo.com/pop-arte/musica/the-town/2025/noticia/2025/08/20/the-town-2025-oferece-infraestrutura-acessivel-e-servicos-para-pessoas-com-deficiencia.ghtml'},
    {'categoria': 'LANÇAMENTO','alt': 'Capa albúm The Life of a Showgirl', 'titulo': 'Taylor Swift anuncia 12º álbum', 'img': 'https://imgs.search.brave.com/MG4B734V5ewTIjkGUiUmCG7BD2KyE9WhbEGh9bN3huU/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9wcmV2/aWV3LnJlZGQuaXQv/dGhlLWxpZmUtb2Yt/YS1zaG93Z2lybC1v/dXQtb2N0b2Jlci0z/cmQtdjAtaGdqdGpn/MGxjdmlmMS5qcGc_/d2lkdGg9NjQwJmNy/b3A9c21hcnQmYXV0/bz13ZWJwJnM9YzYz/ZGUwNzg0MjIwODIx/NzJiMzY2YmQ5NWEw/YjE4N2I3YmE1ZDFj/Mg', 'url' : 'https://g1.globo.com/pop-arte/musica/noticia/2025/08/12/taylor-swift-anuncia-lancamento-do-12o-album.ghtml' },
    {'categoria': 'FESTIVAL', 'alt': 'Primavera Sound', 'titulo': 'Primavera Sound São Paulo 2025?', 'img': 'https://imgs.search.brave.com/nDN3BuLHFjbshIFF2aGoIvswS45POB6d4mfS9YxZsUk/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9mLmku/dW9sLmNvbS5ici9m/b3RvZ3JhZmlhLzIw/MjEvMTIvMDkvMTYz/OTA1NzkwOTYxYjIw/OWY1NjEwN2JfMTYz/OTA1NzkwOV8zeDJf/bWQuanBn', 'url': 'https://cadernopop.com.br/primavera-sound-sao-paulo-2025-saiba-qual-seria-o-nosso-line-up-dos-sonhos/' }
    ]
    return jsonify(banner)

@app.route('/api/artistas')
def api_artistas():
    artistas = [
    {'nome': 'Bruno Mars', 'foto': 'https://preview.redd.it/what-is-your-favorite-bruno-mars-pic-this-is-my-fav-and-its-v0-p3impgmpeygd1.jpeg?width=1080&crop=smart&auto=webp&s=6b926af4249d70f30cde1efe7f17c381e88ea6dd'}, 
    {'nome': 'Lady Gaga', 'foto': "https://imgs.search.brave.com/ueu5h-r-SHSXNiCS6wA83A6a3EGnzS_qsBCSLNRzPjI/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly93d3cu/dmFnYWx1bWUuY29t/LmJyL2xhZHktZ2Fn/YS9kaXNjb2dyYWZp/YS9tYXloZW0ud2Vi/cA"}, 
    {'nome': 'The Weekend', 'foto':"https://imgs.search.brave.com/QdOgKqmehK9w3DpTb-tn_SplDf1TuhyVuGomD3PCNHc/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly93YWxs/cGFwZXJjYXQuY29t/L3cvZnVsbC9lLzAv/NC8xOTM4NzEtMTky/MHgxMDgwLWRlc2t0/b3AtMTA4MHAtdGhl/LXdlZWtuZC13YWxs/cGFwZXItaW1hZ2Uu/anBn"},
    {'nome': 'Taylor Swift', 'foto':"https://imgs.search.brave.com/egwKoUW8YEn_pBA3-BXSXm3asgF20znPstGsqv2NPTs/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9mLmku/dW9sLmNvbS5ici9m/b3RvZ3JhZmlhLzIw/MjQvMTAvMTQvMTcy/ODkxMjc1NTY3MGQx/ZDczYjlkZTlfMTcy/ODkxMjc1NV8zeDJf/bWQuanBn"}, 
    {'nome': 'Tyler, The Creator', 'foto': "https://imgs.search.brave.com/7l8ny5Ca_3FacL4kk7EmUkuO5O9zr6TSYHSd-iUuVbc/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTM2/ODE1NjU3NC9waG90/by9ob2xseXdvb2Qt/Y2FsaWZvcm5pYS10/eWxlci10aGUtY3Jl/YXRvci1hdHRlbmRz/LXRoZS11LXMtcHJl/bWllcmUtb2YtamFj/a2Fzcy1mb3JldmVy/LWF0LXRjbC5qcGc_/cz02MTJ4NjEyJnc9/MCZrPTIwJmM9Q201/TEI0THJNdXViOWtG/SlFuQUI3VjFhSGJS/R1Z4V040VVlSaEd5/azBpRT0"}, 
    {'nome': 'Kendrick Lamar', 'foto': "https://imgs.search.brave.com/QRXAvefHOvqenz7H7kNUull3IbpfevlIPOI9NuhWDf8/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9wcmV2/aWV3LnJlZGQuaXQv/d2hhdHMtdGhlLWhh/cmRlc3Qta2VuZHJp/Y2stbGFtYXItcGlj/dHVyZS15b3UtaGF2/ZS1zZWVuLXYwLXhp/ejR3d3Y3bWg1YjEu/anBlZz93aWR0aD0x/MTI1JmZvcm1hdD1w/anBnJmF1dG89d2Vi/cCZzPWI2NjQ2YzRh/ODRmYjU3Zjc3NDll/MmQ5Mjc0NGMzZTkx/ZGJkNmEzYjg"}, 
    {'nome': 'Sabrina Carpenter', 'foto': "https://imgs.search.brave.com/DH3jKbwjxfS13WQ8wGjGzQX4Mjp-BDZbO8EDaZg_bLo/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pLnBp/bmltZy5jb20vb3Jp/Z2luYWxzLzJmLzU2/L2Q5LzJmNTZkOTc2/YjZmYzljODJjYWEy/MmI0OTg2MTQxMDhk/LmpwZw"}, 
    {'nome': "Alex Turner", 'foto': "https://imgs.search.brave.com/lyV1u_34kp-x0F_1rn24Kcf33f3Rm_5D4snvz2O91Xc/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly93YWxs/cGFwZXJiYXQuY29t/L2ltZy85NzIxMjQ0/LWFyY3RpYy1tb25r/ZXlzLWFsZXgtdHVy/bmVyLmpwZw"}, 
    {'nome': 'Florence + The Machine', 'foto': "https://imgs.search.brave.com/MFF4JtXn54H0IHS5wQcPc26HIK1A2CM6sGVJSJM1niw/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTAz/NTMwOTYwL3B0L2Zv/dG8vZmxvcmVuY2Ut/d2Vsc2gtb2YtZmxv/cmVuY2UtYW5kLXRo/ZS1tYWNoaW5lLXBl/cmZvcm1zLWR1cmlu/Zy1kYXktb25lLW9m/LXYtZmVzdGl2YWwt/MjAxMC1vbi1hdWd1/c3QuanBnP3M9NjEy/eDYxMiZ3PTAmaz0y/MCZjPWtCdU9Rc2dM/UEE0T05mLVZINVRP/amJtNVZhaUtER2N1/bm9Zc3BKODZvS2M9"}, 
    {'nome': 'Mitski', 'foto':"https://imgs.search.brave.com/tHMTQDs1UvCyfk5jOp7ZPVSfaJKpYctH_XGoEhNLgHM/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pLnBp/bmltZy5jb20vb3Jp/Z2luYWxzLzFhLzFl/LzJmLzFhMWUyZjM4/Y2Q3MWIyNjU0MzBj/YzkwODUzMmViYTEz/LmpwZw"}
    ]
    return jsonify(artistas)

@app.route('/api/destaques')
def api_destaques():
    destaques = [
    {'alt': 'SZA', 'categoria': 'Notícias', 'titulo': '100 semanas no Top 10: SZA quebra recorde na Billboard', 'img': 'https://imgs.search.brave.com/q0mvHIZZHv9SazSgAwWP4FYSWntf9J-eXYIwmp7l1HM/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTgx/NzQxMTA2OC9waG90/by9zemEtYXQtdmFy/aWV0eS1oaXRtYWtl/cnMtcHJlc2VudGVk/LWJ5LXNvbnktYXVk/aW8taGVsZC1hdC1u/eWEtd2VzdC1vbi1k/ZWNlbWJlci0yLTIw/MjMtaW4tbG9zLmpw/Zz9zPTYxMng2MTIm/dz0wJms9MjAmYz0x/bm90Q1dJa044c3VI/aHRsVXFXYk1Xbkg0/RFNCWUpzb0d6QWFQ/Tjk2LU5nPQ'},
    {'alt': 'Lollapalooza', 'categoria': 'Eventos', 'titulo': 'Lollapalooza Brasil 2026: venda de ingressos começa na quinta-feira', 'img': 'https://imgs.search.brave.com/eG3U_EIWBeHdgjOQqF8WvdEhiCvTHm9txbvv0XKRwn4/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9iaWxs/Ym9hcmQuY29tLmJy/L3dwLWNvbnRlbnQv/dXBsb2Fkcy8yMDI0/LzA3LzIwMjItMDgt/MDlUMTU0ODAwWl85/ODUwMjEwMjlfTVQx/QUJDUFIwMDBCMDRS/RENfUlRSTUFEUF8z/X0FCQUNBLVBSRVNT/LXNjYWxlZC5qcGc'},
    {'alt': 'Capa Sabrina Carpenter', 'categoria': 'Premiações', 'titulo': '7 artistas confirmados para performances no VMA 2025', 'img': 'https://portalpopline.com.br/wp-content/uploads/2025/06/sabrina-cachorrinha-capa.jpg'}
    ]
    return jsonify(destaques)

@app.route('/api/noticias')
def api_noticias():
    noticias = [
    {'titulo': 'Estudo revela que plantas crescem mais rápido ouvindo heavy metal do que música clássica', 'img': 'https://images.unsplash.com/photo-1604177052603-c2b4cff228db?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aGVBVlklMjBNRVRBTHxlbnwwfDB8MHx8fDA%3D'}, 
    {'titulo': 'Computador "escreveu" uma música que 70% das pessoas acreditaram ser dos Beatles', 'img': 'https://images.unsplash.com/photo-1597577389232-2002664a0aec?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8YmVhdGxlc3xlbnwwfDB8MHx8fDA%3D'},
    {'titulo': 'Cientistas encontram conexão entre ritmo cardíaco e preferência musical', 'img': 'https://plus.unsplash.com/premium_photo-1718349374495-b1d09644f973?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Y2FyZGlhY298ZW58MHwwfDB8fHww'},
    {'titulo': 'Pesquisadores afirmam que o cérebro humano "antecipa" batidas musicais antes delas acontecerem', 'img': 'https://plus.unsplash.com/premium_photo-1690297732590-b9875f77471d?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Y2VyZWJyb3xlbnwwfDB8MHx8fDA%3D'},
    {'titulo': 'Estudo sugere que pessoas que tocam instrumento vivem em média 7 anos a mais', 'img': 'https://images.unsplash.com/photo-1511379938547-c1f69419868d?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW5zdHJ1bWVudG98ZW58MHwwfDB8fHw'},
    {'titulo': 'Fones de ouvido com sensores cerebrais podem criar playlists baseadas no humor do usuário', 'img': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Zm9uZXMlMjBkZSUyMG91dmlkb3xlbnwwfDB8MHx8fDA%3D'}, 
    {'titulo': 'Ouvir música em outra língua melhora a capacidade de aprender idiomas', 'img': 'https://images.unsplash.com/photo-1470225620780-dba8ba36b745?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bSVDMyVCQXNpY2F8ZW58MHwwfDB8fHww'},
    {'titulo': 'Pesquisadores criam algoritmo capaz de prever qual música será um hit em até 80% dos casos', 'img': 'https://plus.unsplash.com/premium_photo-1661882403999-46081e67c401?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8YWxnb3JpdG1vfGVufDB8MHwwfHx8MA%3D%3D'},
    {'titulo': 'Pesquisadores afirmam que ouvir 10 minutos de funk melhora a memória de curto prazo', 'img': 'https://images.unsplash.com/photo-1483821838526-8d9756a6e1ed?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8ZnVua3xlbnwwfDB8MHx8fDA%3D '}
    ]
    return jsonify(noticias)

@app.route('/api/eventos')
def api_eventos():
    eventos = [
    {'titulo': 'Festival secreto no deserto só aceita público que chega de balão','img': 'https://images.unsplash.com/photo-1497531551184-06b252e1bee1?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8YmFsJUMzJUEzb3xlbnwwfDB8MHx8fDA%3D'},
    {'titulo': 'Show surpresa em alto-mar reúne 5 bandas em um navio que não divulgou a rota','img': 'https://images.unsplash.com/photo-1511316695145-4992006ffddb?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y3J1emVpcm98ZW58MHwwfDB8fHww'},
    {'titulo': 'Primeiro festival totalmente silencioso atrai milhares de pessoas','img': 'https://images.unsplash.com/photo-1470229722913-7c0e2dbbafd3?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8ZmVzdGl2YWx8ZW58MHwwfDB8fHww'},
    {'titulo': 'Concerto experimental usou drones como instrumentos musicais','img': 'https://plus.unsplash.com/premium_photo-1714618849685-89cad85746b1?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZHJvbmV8ZW58MHwwfDB8fHww'},
    {'titulo': 'Evento futurista transmitiu um show inteiro em realidade aumentada no céu noturno','img': 'https://plus.unsplash.com/premium_photo-1663091701962-2ae72a2ad2ac?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cmVhbGlkYWRlJTIwYXVtZW50YWRhfGVufDB8MHwwfHx8MA%3D%3D'},
    {'titulo': 'Festival anunciou line-up formado 100% por hologramas de artistas já falecidos','img': 'https://plus.unsplash.com/premium_photo-1682095924383-f4aa9387cc15?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8aG9sb2dyYW1hc3xlbnwwfDB8MHx8fDA%3D'},
    {'titulo': 'Concerto embaixo d’água permite que público ouça músicas apenas por vibração sonora','img': 'https://plus.unsplash.com/premium_photo-1663011158210-e80ee57cfeb4?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cGVzc29hcyUyMGVtYmFpeG8lMjBkYWd1YXxlbnwwfDB8MHx8fDA%3D'},
    {'titulo': 'Evento reúne orquestra sinfônica e DJs tocando simultaneamente em palcos giratórios','img': 'https://images.unsplash.com/photo-1576514129883-2f1d47a65da6?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8cGFsY29zfGVufDB8MHwwfHx8MA%3D%3D'},
    {'titulo': 'Show surpresa em uma estação de metrô paralisou a cidade por 2 horas','img': 'https://plus.unsplash.com/premium_photo-1661876638101-e83e45eaeacc?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8bWV0ciVDMyVCNHxlbnwwfDB8MHx8fDA%3D'},
    ]
    return jsonify(eventos)

@app.route('/api/premiacoes')
def api_premiacoes():
    premiacoes = [
    {'titulo': 'Premiação cria categoria inédita: "Música mais viral do TikTok','img': 'https://images.unsplash.com/photo-1596346599094-4dfa5c61fd0d?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8dGlrdG9rfGVufDB8MHwwfHx8MA%3D%3D'},
    {'titulo': 'Cantor ganha troféu por performance que durou apenas 12 segundos','img': 'https://images.unsplash.com/photo-1665680674724-3a3b3368e036?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8dHJvZmRldXxlbnwwfDB8MHx8fDA%3D'},
    {'titulo': 'Cerimônia anuncia que vencedores serão escolhidos por inteligência artificial','img': 'https://plus.unsplash.com/premium_photo-1683121710572-7723bd2e235d?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8aW50ZWxpZ2VuY2lhJTIwYXJ0aWZpY2lhbHxlbnwwfDB8MHx8fDA%3D'},
    {'titulo': 'Prêmio inusitado reconhece "melhor silêncio dramático em uma música"','img': 'https://images.unsplash.com/photo-1483706600674-e0c87d3fe85b?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8c2lsZW5jaW98ZW58MHwwfDB8fHww'},
    {'titulo': 'Artista recusa troféu e pede para ser premiado com uma pizza gigante no palco','img': 'https://images.unsplash.com/photo-1534308983496-4fabb1a015ee?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8cGl6emF8ZW58MHwwfDB8fHww'},
    {'titulo': 'Premiação secreta acontece em um trem em movimento','img': 'https://images.unsplash.com/photo-1527295110-5145f6b148d0?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8dHJlbXxlbnwwfDB8MHx8fDA%3D'},
    {'titulo': 'Cerimônia anuncia premiação para "melhor capa de álbum gerada por IA"','img': 'https://images.unsplash.com/photo-1697577418970-95d99b5a55cf?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW50ZWxpZ2VuY2lhJTIwYXJ0aWZpY2lhbHxlbnwwfDB8MHx8fDA%3D'},
    {'titulo': 'Troféu de premiação é impresso em 3D em tempo real no palco','img': 'https://images.unsplash.com/photo-1625643268477-838321f445bb?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTF8fHRyb2ZldXxlbnwwfDB8MHx8fDA%3D'},
    {'titulo': 'Cantora vence duas vezes na mesma categoria com músicas lançadas no mesmo mês','img': 'https://images.unsplash.com/photo-1604658243847-17375af581fa?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8dmVuY2Vkb3JhfGVufDB8MHwwfHx8MA%3D%3D'},
    ]
    return jsonify(premiacoes)

if __name__ == '__main__':
    app.run(debug=True)
