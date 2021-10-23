// TRADUÇÃO CAMPOS DE SENHA
var ps1 = document.querySelector('#div_id_password1 > label')
var ps2 = document.querySelector('#div_id_password2 > label')

ps1.innerHTML = "Senha*"
ps2.innerHTML = "Confirme a senha*"

// REQUERIMENTOS SENHA
lista_requerimentos_senha = document.querySelectorAll("li")

lista_requerimentos_senha[3].innerHTML = "Sua senha não pode ser muito similar à suas outra informações"
lista_requerimentos_senha[4].innerHTML = "sua senha precisa conter ao menos 8 caracteres"
lista_requerimentos_senha[5].innerHTML = "Sua senha não pode ser uma senha muito comum"
lista_requerimentos_senha[6].innerHTML = "Sua senha não pode ser completamente numérica"

// SUBTEXTO CONFIRMAÇÃO
var sm = document.querySelectorAll('small')
sm[1].innerHTML = 'Digite a mesma senha de antes, para verificação'

var div_nome_loja = document.getElementById('div_id_nome_da_loja')
div_nome_loja.style.display = 'None'
// NOME DA LOJA 
document.addEventListener('input', function (event) {

	if (event.target.id !== 'id_objetivo') return;

	if (event.target.value === 'Cliente') {
		div_nome_loja.style.display = 'None'
	}

    if (event.target.value === 'Lojista') {
		div_nome_loja.style.display = 'Block'
	}
})