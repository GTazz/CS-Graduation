programa { 
  funcao inicio() 
  {
     inteiro quantidade, i, numero, soma
     real media

     escreva("Digite a quantidade de números: ")
     leia(quantidade)
     
     se (quantidade <= 0) 
     {
     escreva("A lista está vazia")
     retorne
     }
     soma = 0
     para(i = 0; i < quantidade; i++) 
     {
      escreva("Digite um número: ")
      leia(numero)
      soma += numero
     }

     media = soma / quantidade 

     escreva("A média dos números é: ", media)
  }
}
