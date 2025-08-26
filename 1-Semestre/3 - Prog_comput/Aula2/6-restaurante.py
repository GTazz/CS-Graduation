from os import system as cmd


project_title = "CÁLCULO DE GORJETA DO GARÇOM"

cmd("cls")  # Limpa a tela do terminal
t_lines = f"\033[1;34m{"=" * len(project_title)}\033[m"
print(f"{t_lines}\n\033[1;33m{project_title}\n{t_lines}")

bill = float(input("\nDigite o valor gasto no restaurante: R$"))

tip = bill / 100 * 10
total = bill + tip

print(f"\nValor da conta: R${bill:.2f}\nGorjeta 10%: R${tip:.2f}\nTotal: R${total:.2f}\n")
