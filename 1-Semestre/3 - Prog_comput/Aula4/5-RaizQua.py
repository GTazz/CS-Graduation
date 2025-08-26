from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("Raiz quadrada")

num = int(input("Digite um número: "))
if num < 0:
    print("\nNão existe raiz quadrada de número negativo.\n")
else:
    print(f"\nA raiz quadrada de {num} é: {f"{num ** 0.5:.2f}".rstrip("0").rstrip(".")}\n")
