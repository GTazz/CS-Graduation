from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("Comissão de vendas")

salary = float(input("Salário fixo do funcionário: R$"))
commission = float(input("Quantidade de vendas: R$")) * 0.04

total = salary + commission

print(f"\nComissão: R${commission:.2f}\nTotal: R${total:.2f}\n")
