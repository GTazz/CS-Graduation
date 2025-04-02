from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("Maior número")

n1 =  int(input("Digite o primeiro número: "))
n2 =  int(input("Digite o segundo número: "))
n3 =  int(input("Digite o terceiro número: "))

print(f"\n{n1 if n2<n1>n3 else n2 if n1<n2>n3 else n3 if n1<n3>n2 else "Nenhum valor individual"} é o maior.\n")
