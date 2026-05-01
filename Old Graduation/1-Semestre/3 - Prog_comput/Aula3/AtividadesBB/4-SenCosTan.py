from os import system as cmd
from math import radians, sin, cos, tan


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls") # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("Seno Cosseno e Tangente")

angle = float(input("Digite o valor do ângulo em graus: "))

angle_rad = radians(angle)

_sin = sin(angle_rad)
_cos = cos(angle_rad)
_tan = tan(angle_rad)

print(f"""
Seno: {_sin:.3f}
Cosseno: {_cos:.3f}
Tangente: {_tan:.3f}
""")
