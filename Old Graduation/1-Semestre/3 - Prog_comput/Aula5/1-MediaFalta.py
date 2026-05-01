from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("Status do aluno falta / nota")

med = round(float(input("Digite a média do aluno: ")))
freq_percent = float(input("Digite o percentual de frequência do aluno: "))

result_str = "Reprovado por falta!" if freq_percent < 75 else "Reprovado por nota!" if med < 6 else "Aprovado!"

print(f"\n{result_str}\n")
