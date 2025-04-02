from os import system as cmd


project_title = "CONVERSOR DE REAL PARA DÓLAR"

cmd("cls")  # Limpa a tela do terminal
t_lines = f"\033[1;34m{"=" * len(project_title)}\033[m"
print(f"{t_lines}\n\033[1;33m{project_title}\n{t_lines}")

exchange_rate = float(input("\nDigite a cotação atual do dollar: $"))

reais = float(input("\nDigite o valor em reais a ser convertido: R$"))
dollar = reais / exchange_rate

print(f"\nValor em dólar: ${dollar:.2f}\n")
