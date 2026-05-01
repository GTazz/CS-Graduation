from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("Média de 10 alunos")

c = 1
while c <= 10:
    grade = 0
    for i in range(1, 3):
        grade = float(input(f"{c}º aluno, nota {i}: ")) + grade
    print(f"\nMédia do {c}º aluno: {round(grade/2)}\n")
    c += 1
