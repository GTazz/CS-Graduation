from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls") # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("Volume tronco de piramide")

h = float(input("Digite a altura do tronco de pirâmide: "))
b_bigger = float(input("Digite a base maior do tronco de pirâmide: "))
b_smaller = float(input("Digite a base menor do tronco de pirâmide: "))

volume =h/3*(b_bigger**2 + b_smaller**2 + (b_bigger**2 * b_smaller**2)**0.5) 

print(f"\nO volume do tronco de pirâmide é: {volume:.2f}\n")
