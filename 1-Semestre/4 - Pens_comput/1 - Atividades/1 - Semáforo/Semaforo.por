programa {
  inclua biblioteca Util

  cadeia corFarolCarro, corFarolPedestre
  inteiro segundos

  funcao mudarFarol () {

    // Aguardar tempo de semáforo e mostra tempo na tela
    para (inteiro i = segundos; i >= 0; i--) {  
      Util.aguarde(1000)
      escreva("\n\n\n\n\n\n\nPassagem de carro em: ", corFarolCarro)
      escreva("\nPassagem de pedestre: ", corFarolPedestre)
      escreva("\nContagem regressiva ", i)
    }       
  }
  
  funcao inicio() 
  {
    enquanto (verdadeiro) {
      se (corFarolCarro == "verde") {
        corFarolCarro = "amarelo"
        corFarolPedestre = "vermelho"
        segundos = 5
      } senao se (corFarolCarro == "amarelo") {
        corFarolCarro = "vermelho"
        corFarolPedestre = "verde"
        segundos = 10
      } senao {
        corFarolCarro = "verde"
        corFarolPedestre = "vermelho"
        segundos = 20
      }
      mudarFarol()
    }
  }
}

