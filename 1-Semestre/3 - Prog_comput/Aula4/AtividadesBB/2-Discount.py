from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls") # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("Desconto acima de R$200")

value = float(input("Digite o valor da compra: R$"))

if value > 200:
    discount = value * 0.2
    new_value = value - discount
    print(f"\nVocê recebeu um desconto de 20%. O valor final da compra é: R${new_value:.2f}\n")

else:
    print(f"\nNão há desconto. O valor da compra é: R${value:.2f}\n")
