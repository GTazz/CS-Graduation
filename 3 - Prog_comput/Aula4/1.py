from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("")

# Solicita os valores das contas e do salário
conta1 = float(input("Digite o valor da primeira conta: "))
conta2 = float(input("Digite o valor da segunda conta: "))
conta3 = float(input("Digite o valor da terceira conta: "))
salario = float(input("Digite o valor do seu salário: "))

# Calcula o total das contas e verifica se o salário é suficiente
total_contas = conta1 + conta2 + conta3

if salario >= total_contas:
    restante = salario - total_contas
    print(f"Salário suficiente! O valor restante é: R$ {restante:.2f}")
else:
    print("Salário insuficiente!")