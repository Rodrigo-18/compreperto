const rua         = document.querySelector("input[name='nome_rua']")
const complemento = document.querySelector("input[name='complemento']")
const botao       = document.querySelector("#confirmar-button")
const divDetalhes = document.querySelector("#pedido-detalhes")

rua.addEventListener('change', () => {
  if (rua.value.length > 60) {
    botao.disabled = true
  } else {
    botao.disabled = false
  }
})

complemento.addEventListener('change', () => {
  if (complemento.value.length > 60) {
    botao.disabled = true
  } else {
    botao.disabled = false
  }
})
