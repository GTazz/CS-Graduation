from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("Conversão Bin => Dec")

num = str(int(input(f"Digite um úmero em binário: "))).strip("0")
decimal = 0
for i, n in enumerate(num[::-1]):
    if n not in "01":
        print("\nEsse número não é binário!\n")
        exit()
    decimal += int(n)*2**i

print(f"\nBinário {num} para Decimal: {decimal}\n")
