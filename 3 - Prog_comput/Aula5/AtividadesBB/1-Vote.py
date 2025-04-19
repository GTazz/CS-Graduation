from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("Classe eleitoral", "<>-+-")

age = int(input("Digite a sua idade: "))

if 0 < age < 16:
    print("\nVocê não pode votar!\n")
elif 18 <= age <= 65:
    print("\nVocê é obrigado a votar\n")
elif 16 <= age <= 18 or age > 65:
    print("\nVocê Vota se quiser\n")
else:
    print("\nIdade inválida!\n")
    