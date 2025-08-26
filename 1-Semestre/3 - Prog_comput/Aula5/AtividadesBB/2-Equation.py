from os import system as cmd
from math import sqrt


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("Equação de 2º grau")

a = int(input("Digite o valor de a: "))

if a == 0:
    print("\nNão é equação do segundo grau\n")
else:
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
    delta = b**2 - 4*a*c

    if delta < 0:
        print("\nNão há raízes reais\n")
    elif delta == 0:
        raiz = -b / (2*a)
        print(f"\nA equação possui uma única raiz real: {raiz}\n")
    else:
        raiz1 = (-b + sqrt(delta)) / (2*a)
        raiz2 = (-b - sqrt(delta)) / (2*a)
        print(f"\nAs raízes da equação são: {raiz1}, {raiz2}\n")
