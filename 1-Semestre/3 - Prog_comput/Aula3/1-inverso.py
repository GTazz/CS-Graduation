from os import system as cmd


def print_title(prjct_title, style="="):
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("Inverso", "-x-=")

num = int(input("Digite um número: "))
print()

d0 = num // 1000
print(d0)
d1 = num % 1000 // 100
print(d1)
d2 = num % 100 // 10
print(d2)
d3 = num % 10
print(d3)

inverted = d3 * 1000 + d2 * 100 + d1 * 10 + d0

print(f"\nO número {num} invertido é: {inverted}\n")
