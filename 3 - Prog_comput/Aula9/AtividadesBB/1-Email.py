from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


while True:
    try:
        print_title("Exibir domínio do e-mail")
        email = input("Digite o seu e-mail: ")
        domain = "\033[4;34mhttp://" + email.split("@")[1] + "\033[m"
    except IndexError:
        continue
    if "." not in domain:
        continue   
    break

print(f"\nO domínio do e-mail digitado é: {domain}\n")
