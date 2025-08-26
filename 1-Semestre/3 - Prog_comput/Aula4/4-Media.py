from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("Média")

MED = 6

num1 = float(input("Digite a primeira nota: "))
num2 = float(input("Digite a segunda nota: "))

media = round(num1 + num2 / 2)
# med_str = f"{media:.2f}".rstrip("0").rstrip(".")

if media >= MED:
    print(f"\nA média é {media}, aluno aprovado.\n")
else:
    print(f"\nA média é {media}, aluno reprovado.\n")