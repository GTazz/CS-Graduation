#include <stdio.h>

int main() {
    int a1, a2, a3, maiorNota, soma;
    const char* maiorNotaChar;

    printf("Calculadora de Notas\n");

    // Solicitar input da nota a1
    printf("\nDigite a nota da A1 (0 à 5): ");
    scanf("%i", &a1);

    // Solicitar input da nota a2
    printf("Digite a nota da A2 (0 à 5): ");
    scanf("%i", &a2);

    // Calcular a média de a1 e a2
    soma = a1 + a2;  // Correção aqui, divisão por 2

    // Exibir as notas e a média
    printf("\nNota A1: %i\n", a1);  // Corrigido para imprimir as variáveis
    printf("Nota A2: %i\n", a2);  // Corrigido para imprimir as variáveis
    printf("Somatória: %i\n", soma);  // Corrigido para imprimir a média

    // Determinar a situação do aluno
    if (soma >= 6) {
        printf("Situacao: APROVADO\n");
    } else if (soma == 5) {  // Correção de 'final' para 'media'
        printf("\nSituacao: AF / EM RECUPERAÇÃO\n");
        
        printf("\nNota da prova de recuperção: ");
        scanf("%i", &a3);
        
        // Definir a maior nota entre a1 e a2
        if (a1 > a2) {
           maiorNota = a1;
           maiorNotaChar = "A1";
        } else {
           maiorNota = a2;
           maiorNotaChar = "A2";
        }
        soma = a3 + maiorNota;  // Correção aqui, divisão por 2
        
        // Exibir as notas e a média
        printf("\nNota %s: %i\n", maiorNotaChar, maiorNota); 
        printf("Nota A3: %i\n", a3);
        printf("Somatória: %i\n", soma);  // Corrigido para imprimir a média    
            
        // Determinar a situação do aluno
        if (soma >= 6) {
            printf("\nSituacao: APROVADO\n");
        } else {
            printf("\nSituacao: REPROVADO\n");
        }
        
    } else {
        printf("Situacao: REPROVADO\n");
        
    }
    printf("\nPrograma encerrado.\n");

    return 0;
}