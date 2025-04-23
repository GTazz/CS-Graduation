from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("Exibir lucro formatado")

prod = float(input("Digite o valor do custo de produção: "))
faturamento = float(input("Digite o valor do faturamento: "))

lucro = f"R$ {faturamento - prod:_.2f}".replace(".", ",").replace("_", ".")

print(f"\nO lucro é de: {lucro}\n")

num1 = int(input("1º Número: "))
num2 = int(input("2º Número: "))