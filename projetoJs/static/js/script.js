let email=document.getElementById('email')
let user=document.getElementById('username')
let senha=document.getElementById('password')
let mensagemText =document.getElementById("mensagem");
let botao=document.getElementById('botao')
let form=document.getElementById('form')

function validarMensagem(){
    console.log("to na validacao")
    if (!email.value || !user.value || !senha.value) {
        //alert("oi")
        mensagemText.innerText = "Por favor, preencha todos os campos.";
        mensagemText.style.color = "red";
        console.log("dd")
        return; 

    }
    let valor=email.value
    if (!valor.includes("@gmail.com")&&!valor.includes("@yahoo.com")&&!valor.includes("@hotmail.com")){
       // alert("tchau")
        mensagemText.innerText = "Por favor, preencha o email corretamente.";
        mensagemText.style.color = "red";
        console.log("dd")
        return; 
    }

}

botao.addEventListener("click", (e)=>{
   // e.preventDefault()
    validarMensagem()
})
