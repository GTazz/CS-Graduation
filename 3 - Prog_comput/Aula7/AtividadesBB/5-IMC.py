from math import trunc
from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("IMC homem e mulher")

gender = input("Seu sexo é Masculino ou Feminino? [M/F] ").strip()[0].upper()
height = float(input("Informe sua altura em Metros: "))

weight = (72.7*height) - 58 if gender == "M" else (62.1*height) - 44.7

print(f"\nO peso ideal para você seria {weight:.2f}\n")