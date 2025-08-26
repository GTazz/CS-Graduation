from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls") # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("Prestações em atraso")

value_invoice = float(input("Digite o valor da prestação: "))
fee = float(input("Digite a porcentagem de multa pelo atraso: "))
fee_days = int(input("Digite a quantidade de dias de atraso: "))

invoice = value_invoice + (value_invoice * (fee / 100) * fee_days)

print(f"\nO valor da prestação atualizado é: R${invoice:.2f}\n")
