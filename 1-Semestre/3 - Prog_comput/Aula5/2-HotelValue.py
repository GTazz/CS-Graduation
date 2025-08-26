from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("Valor da diária de um hotel")

room_type = input("Digite o tipo de quarto [Simples, Duplo ou Triplo]: ").lstrip()[0].upper()
days = int(input("Digite a quantidade de dias: "))

if room_type == "S":
    price = 255.5
    room_type = "simples"
elif room_type == "D":
    price = 305.5
    room_type = "duplo"
elif room_type == "T":
    price = 360.5
    room_type = "triplo"
else:
    print("\nTipo de quarto inválido!\n")
    exit()

total_price = price * days

print(f"\nO valor da diária do quarto {room_type} é R${price:.2f}\n{days} dias custam R${total_price:.2f}\n")
