from os import system as cmd


project_title = "CONVERSOR DE CELSIUS PARA FAHRENHEIT E KELVIN"

cmd("cls")  # Limpa a tela do terminal
t_lines = f"\033[1;34m{"=" * len(project_title)}\033[m"
print(f"{t_lines}\n\033[1;33m{project_title}\n{t_lines}")

tc = float(input("\nDigite uma temperatura em Celsius: "))

tf = tc * 1.8 + 32
tk = tc + 273

print(f"\nTemperatura em Fahrenheit: {tf:.2f}\nTemperatura em Kelvin: {tk:.2f}\n")
