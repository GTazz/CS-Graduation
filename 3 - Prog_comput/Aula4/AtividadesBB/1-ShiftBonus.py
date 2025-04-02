from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls") # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


def error_shift():
    raise Exception("Turno inválido")

print_title("Bonus noturno")

shift = input("Informe o turno de trabalho [\"Noturno\", \"Diurno\"]: ").lstrip()[0].upper()
val_hour = 45.00 if shift == 'N' else 37.50 if shift == 'D' else error_shift()

hours_work = float(input("Informe a quantidade de horas trabalhadas: "))
salary = hours_work * val_hour

print(f"\nO salário calculado é: R${salary:.2f}\n")
