from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("Alunos | Sistema de voto")

len_students = int(input("Quantos alunos tem na escola? "))
print()

students_vote = 0
students_noVote = []
for i in range(1, len_students+1):
    age = int(input(f"{i}º Aluno, idade: "))
    if age >= 16:
        students_vote += 1
    else:
        students_noVote += [age]


print(f"\n{students_vote} Alunos podem votar.")

if len(students_noVote) != 0:
    students_noVote = round(sum(students_noVote) / (len(students_noVote)))
    print(f"{students_noVote} É a idade média dos alunos que não votam.\n")
else:
    print("Todos os alunos votam.\n")
    