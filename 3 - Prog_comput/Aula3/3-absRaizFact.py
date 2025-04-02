from os import system as cmd
from math import sqrt, factorial


def print_title(prjct_title: str, style: str="="):
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("absoluto, raiz e fatorial", "-x-=")

num = float(input("Digite um número: "))

num_abs = abs(num)
num_int = int(num)
num_sqrt = sqrt(num)
num_fact = factorial(int(num))

print(f"""
VALORES DE {num}:
 
Absoluto; {num_abs}
Inteiro; {num_int}
Raiz; {f"{num_sqrt:.2f}".rstrip("0").rstrip(".")}
Fatorial; {num_fact}
""")

num_fact = 1
for i in range(1, num_int+1):
    num_fact *= i

print(f"Fatorial por loop: {num_fact}\n")	