from os import system as cmd


project_title = "CÁLCULO DE VELOCIDADE MÉDIA"

cmd("cls")  # Limpa a tela do terminal
t_lines = f"\033[1;34m{'=' * len(project_title)}\033[m"
print(f"{t_lines}\n\033[1;33m{project_title}\n{t_lines}")

distance = float(input("\nDigite a distância entre as duas cidades (em km): "))
time = float(input("\nDigite o tempo gasto na viagem (em horas): "))

average_time = distance / time

print(f"\nA velocidade média do veículo foi de {average_time:.2f}km/h\n")
