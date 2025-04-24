from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


while True:
    try:
        print_title("Somando um número com sua versão inversa", "+-0-+-1-")
        
        num = "".join(input("Digite um número inteiro de três algarismos: ").split()).lstrip("+")
        if len(num.lstrip("-")) != 3:
            continue
        
        num_rev = int(num[::-1]) if num[0] != "-" else int("-" + num[:0:-1])
        num = int(num)
    except ValueError:
        continue
    break

print(f"\nSoma: {num} + {num_rev} = \033[4m{num + num_rev}\033[m\n")
