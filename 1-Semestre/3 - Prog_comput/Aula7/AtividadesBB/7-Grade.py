from math import ceil
from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("Notas de 'A' à 'E'")

grade1 = float(input("1º Nota: "))
grade2 = float(input("2º Nota: "))

grade = (grade1 + grade2) / 2

if 9 <= grade >= 10:
    grade = "A"
    status = "APROVADO"
elif 7.5 <= grade < 9:
    grade = "B"
    status = "APROVADO"
elif 6 <= grade < 7.5:
    grade = "C"
    status = "APROVADO"
elif 4 <= grade < 6:
    grade = "D"
    status = "REPROVADO"
elif 0 <= grade < 4:
    grade = "E"
    status = "REPROVADO"
    
print(f"\nNota do Aluno: {grade}\nO aluno foi {status}!\n")
