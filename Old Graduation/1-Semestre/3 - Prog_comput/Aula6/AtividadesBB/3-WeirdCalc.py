from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("Iteração numérica dinâmica")

num = int(input("Digite o número: ")) + 1
if num < 2:
    print("\nNúmero inválido!!\n")
else:
    s = 1
    str_calc = "1"
    for i in range(1, num):
        s += 1/i
        str_calc += f" + 1/{i}"
        
    print(f"\nS = {str_calc} = {s:.2f}\n")
