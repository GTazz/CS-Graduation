from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("Cálculo de imc")

weight = float(input("Digite o seu peso (kg): "))
height = float(input("Digite a sua altura (m): "))

imc = weight / height**2

print(f"\nSeu IMC é {imc:.2f}.\nVocê está ", end="")

if imc < 20:
    print("abaixo do peso.\n")
elif imc < 25:
    print("com o peso normal.\n")
elif imc < 30:
    print("com sobrepeso.\n")
elif imc < 40:
    print("obesidade.\n")
else:
    print("obesidade mórbida.\n")
