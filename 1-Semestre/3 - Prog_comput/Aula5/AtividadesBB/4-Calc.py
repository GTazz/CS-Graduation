from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


TITLE = "Calculadora"
print_title(TITLE)

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

while 1:
    operation = input("Escolha a operação ('+', '-', '*', '/'): ").strip()
    if operation in ('+', '-', '*', '/'): 
        break
    print_title(TITLE)


if num2 == 0:
    print("\nErro: Divisão por zero não é permitida.\n")
else:
    str_calc = f"{num1} {operation} {num2}"
    result = eval(str_calc)
    
    print(f"\n{str_calc} = {result:.2f}\n")
