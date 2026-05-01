from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas



while True:
    try:
        print_title(" Verifica ano bissexto ", "-=-/")
        year = int("".join(input("Digite um ano: ").split()))
    except ValueError:
        continue
    if year < 1:
        continue
    break

print(
    f"\n\033[1;32mO ano {year} é bissexto!\033[m\n" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 
    f"\n\033[1;31mO ano {year} não é bissexto!\033[m\n"
)
