from os import system as cmd


project_title = "CÁLCULO DE ÁREA DE RETÂNGULO"

cmd("cls")  # Limpa a tela do terminal
t_lines = f"\033[1;34m{"=" * len(project_title)}\033[m"
print(f"{t_lines}\n\033[1;33m{project_title}\n{t_lines}")

print(
    """
     x
 _________
|         |
|         |  y
|         |
|_________|
"""
)

x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))

area: float = x * y

cmd("cls")
print(f"{t_lines}\n\033[1;33m{project_title}\n{t_lines}")

print(
    f"""
     x = {x:.2f}
 _________
|         |
|         |  y = {y:.2f}
|         |
|_________|
"""
)
print(f"Área do {"retângulo" if x != y else "quadrado"}: {area:.2f}\n")
