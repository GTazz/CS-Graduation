from os import system as cmd
from difflib import get_close_matches


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas

def close_to(str_input, str_list):
    closer = get_close_matches(str_input, str_list, n=1, cutoff=0.6)
    return closer[0] if closer else None


TITLE = "Dados de altura entre homens e mulheres"

people = []
i = 1
while True:
    print_title(TITLE)
    sex = close_to(input(f"Digite o sexo da {i}º pessoa (M para masculino, F para feminino ou S para sair): ").strip().lower(), ("m", "f", "s"))
    if sex == 's':
        print_title(TITLE)
        break
    if sex not in ['m', 'f']:
        print("Entrada inválida. Tente novamente.")
        continue
    
    height = float(input("Digite a altura da pessoa (em metros): "))
    people += [[sex, height]]
    i += 1

if not people:
    print("Nenhuma pessoa foi registrada.\n")
else:
    men_heights = [height for sex, height in people if sex == 'm']
    women_heights = [height for sex, height in people if sex == 'f']

    print(f"Dados cadastrados: {people}\n")

    if men_heights:
        print(f"Altura média dos homens: {sum(men_heights) / len(men_heights):.2f} metros")
    else:
        print("Nenhum homem foi registrado.")

    if women_heights:
        print(f"Altura média das mulheres: {sum(women_heights) / len(women_heights):.2f} metros\n")
    else:
        print("Nenhuma mulher foi registrada.\n")
