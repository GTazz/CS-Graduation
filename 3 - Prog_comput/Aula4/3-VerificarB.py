from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("Verificar B")

a = int(input("Valor de A: "))
b = int(input("Valor de B: "))
c = int(input("Valor de C: "))

if a > b < c:
    print(f"\nO menor valor é B = {b}\n")
