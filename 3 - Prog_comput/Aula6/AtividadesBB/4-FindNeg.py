from os import system as cmd
from difflib import get_close_matches


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas

def close_to(str_input, str_list):
    closer = get_close_matches(str_input, str_list, n=1, cutoff=0.6)
    return closer[0] if closer else None


TITLE = "Encontrar valores negativos e menor valor"

E_LOOP = ["exit", "e"]
values = []
i = 1
while True:
    print_title(TITLE)
    value = input(f"Digite o {i}º um valor real [\"exit\" para sair]: ").strip().lower()
    if close_to(value, E_LOOP) in E_LOOP:
        print_title(TITLE)
        break
    values += [float(value)]
    i += 1

if values:
    positives = sum(1 for v in values if v > 0)
    negatives = sum(1 for v in values if v < 0)
    smallest = min(values)

    print(f"Valores digitados: {values}\n")
    print(f"Quantidade de valores positivos: {positives}")
    print(f"Quantidade de valores negativos: {negatives}")
    print(f"Menor valor: {smallest:.2f}\n")
else:
    print("Nenhum valor foi inserido.\n")
