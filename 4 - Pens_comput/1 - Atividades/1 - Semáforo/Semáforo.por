programa {
  inclua biblioteca Util

  cadeia corFarolCarro, corFarolPedestre
  inteiro segundos

  funcao mudarFarol (cadeia corCarro, inteiro segundosCarro) {

    se (corCarro == "vermelho") {
      corFarolPedestre = "verde"
    } senao {
      corFarolPedestre = "vermelho"
    }

    // Aguardar tempo de semáforo e mostra tempo na tela]
    para (inteiro i = segundosCarro; i >= 0; i--) {  
      Util.aguarde(1000)
      escreva("\n\n\n\n\n\n\nPassagem de carro em: ", corCarro)
      escreva("\nPassagem de pedestre: ", corFarolPedestre)
      escreva("\nContagem regressiva ", i)
    }       
  }
  
  funcao inicio() 
  {
    enquanto (verdadeiro) {
      se (corFarolCarro == "verde") {
        corFarolCarro = "amarelo"
        segundos = 5 // 15
      } senao se (corFarolCarro == "amarelo") {
        corFarolCarro = "vermelho"
        segundos = 5 // 45
      } senao {
        corFarolCarro = "verde"
        segundos = 5 // 30
      }
      mudarFarol(corFarolCarro, segundos)
    }
  }
}

