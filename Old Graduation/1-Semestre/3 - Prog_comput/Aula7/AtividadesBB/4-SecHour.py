from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("De segundos para horas")

seconds = float(input("Digite um tempo em segundos: "))
hours = seconds // 3600
rest = seconds % 3600
minutes = rest // 60
seconds = rest % 60
formatted = f"{hours}h:{minutes}m:{seconds}s"


print(f"Esse tempo em segundos é equivalente a {hours} horas, {minutes} minutos e {seconds} segundos.\n\nFormatado: {formatted}\n")
