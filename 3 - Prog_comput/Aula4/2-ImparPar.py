from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("impar ou par verificador")

num = int(input("Digite um número inteiro: "))

if num % 2 == 0:
    print(f"\nO número {num} é par.\n")
else:
    print(f"\nO número {num} é ímpar.\n")
