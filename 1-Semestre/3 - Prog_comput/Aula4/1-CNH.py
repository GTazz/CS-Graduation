from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("Cnh verificador de idade")

age = int(input("Digite sua idade: "))

if age >= 18:
    print("\nVocê pode tirar sua CNH.\n")
elif age <=0:
    print("\nVocê nem nasceu ainda! Idade inválida!\n")
else:
    print(f"\nVocê ainda não pode tirar sua CNH, pois ainda falta{"m" if age < 17 else ""} {18 - age} ano{"s" if age < 17 else ""}.\n")

