from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls") # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("Pagar contas")

print("Digite o valor das contas à pagar:\n")

tax_phone = float(input("Telefone: R$"))
tax_water = float(input("    Água: R$"))
tax_light = float(input("     Luz: R$"))
money = float(input("\nDigite o valor que você tem: R$"))

total = tax_phone + tax_water + tax_light

if money >= total:
    print(f"\nVocê pode pagaras contas. Sobra R${money - total:.2f}\n")
else:
    print(f"\nSalário insuficiente!. Faltam R${total - money:.2f}\n")
