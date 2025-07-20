document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('form');
    const mensagem = document.getElementById('mensagem');

    const emailRegexRestrito = /^[^\s@]+@(gmail\.com|hotmail\.com|outlook\.com|yahoo\.com)$/i;

    // Mostra mensagem salva no sessionStorage (se existir)
    const mensagemSalva = sessionStorage.getItem('mensagem');
    if (mensagemSalva) {
        mensagem.textContent = mensagemSalva;
        mensagem.style.color = 'red';
        sessionStorage.removeItem('mensagem');
    }

    form.addEventListener('submit', function (e) {
        const username = document.getElementById('username').value.trim();
        const email = document.getElementById('email').value.trim();
        const password = document.getElementById('password').value.trim();

        mensagem.textContent = '';
        mensagem.style.color = 'red';

        if (!username || !email || !password) {
            sessionStorage.setItem('mensagem', ' Todos os campos são obrigatórios!');
        } else {
            sessionStorage.removeItem('mensagem');
        }

        if (email && !emailRegexRestrito.test(email)) {
            e.preventDefault();
            mensagem.textContent = 'Digite um e-mail válido (gmail, hotmail, outlook, yahoo)!';
        }
    });

    const flashes = document.querySelectorAll('.flash-message');
    flashes.forEach(flash => {
        setTimeout(() => {
            flash.style.transition = 'opacity 0.5s ease';
            flash.style.opacity = '0';
            setTimeout(() => flash.remove(), 500);
        }, 4000);
    });
});


//professor, eu nao entendi direito pq printar duas mensagens de erro, e deu mt trabalho fazer as duas aparecerem (pq o js buga e a msg aparece por menos de 1seg).
// na minha opiniao, somente a mensagem de erro (de campo vazio) do flash deveria aparecer, enquanto o js apenas verifica o email, e impede de enviar caso o esse seja invalido, mas como n era isso que o exercicio pedia, deixei assim. pfvr, se estiver errado, me avise para que eu corrija