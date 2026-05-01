from os import system as cmd
from math import sqrt


def print_title(prjct_title: str, style: str="="):
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("Raiz quadrada", "-x-=")

num = float(input("Digite um número: "))

print(f"\nA raiz quadrada de {f"{num:.2f}".rstrip("0").rstrip(".")} é: {f"{sqrt(num):.2f}".rstrip("0").rstrip(".")}\n")
