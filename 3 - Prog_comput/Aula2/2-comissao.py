from os import system as cmd


project_title = "ACRÉSCIMO SALARIAL COM COMISSÃO"

cmd("cls")  # Limpa a tela do terminal
t_lines = f"\033[1;34m{"=" * len(project_title)}\033[m"
print(f"{t_lines}\n\033[1;33m{project_title}\n{t_lines}")


paycheck = float(input("\nDigite o salário do funcionário: R$"))

commission = paycheck / 100 * 5
total = paycheck + commission

print(f"\nSalário: R${paycheck:.2f}\nComissão 5%: R${commission:.2f}\nTotal: R${total:.2f}\n")
