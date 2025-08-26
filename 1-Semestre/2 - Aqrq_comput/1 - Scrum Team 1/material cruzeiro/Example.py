# Script para avaliar a expressão algébrica: A + B


# Recebendo os inputs booleanos
A = bool(int(input("Digite o valor de A (0 ou 1): ")))
B = bool(int(input("Digite o valor de B (0 ou 1): ")))

# Avaliando a expressão
resultado = A or B

# Exibindo o resultado
print(f"O resultado da expressão é: {resultado}")
