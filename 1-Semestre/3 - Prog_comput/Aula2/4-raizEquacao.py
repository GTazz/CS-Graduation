from os import system as cmd
import math


project_title = "EQUAÇÃO DE SEGUNDO GRAU"

cmd("cls")  # Limpa a tela do terminal
t_lines = f"\033[1;34m{"=" * len(project_title)}\033[m"
print(f"{t_lines}\n\033[1;33m{project_title}\n{t_lines}")

a = float(input("\nDigite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4 * a * c

if delta < 0:
    print("\nAs raízes não são reais\n")
    exit()

sqrt_1 = f"{(-b + math.sqrt(delta)) / (2 * a):.4f}".rstrip("0").rstrip(".")
sqrt_2 = f"{(-b - math.sqrt(delta)) / (2 * a):.4f}".rstrip("0").rstrip(".")

print(f"\nAs raízes da equação são: {{{sqrt_1:}, {sqrt_2:}}}\n")
