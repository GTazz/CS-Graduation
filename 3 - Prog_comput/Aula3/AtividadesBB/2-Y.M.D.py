from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls") # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("Anos, meses e dias de idade")

year = int(input("Digite quantos anos voce tem? "))
month = int(input(f"{year} anos e quantos meses? "))
day = int(input(f"{year} anos, {month} meses e quantos dias? "))

total_days = year * 365 + month * 30 + day

print(f"\nVocê tem {year} anos, {month} meses e {day} dias de idade.\nTotalizando aproximadamente {total_days} dias de vida.\n")
