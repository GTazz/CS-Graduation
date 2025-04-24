from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


while True:
    try:
        print_title("Simulador de Investimentos com Juros Compostos")
        invest = float(input("Digite o valor investido R$ "))
        rate = float(input("Digite a taxa de juros mensal [%]: "))
        months = int(input("Digite o período em meses: "))

        if invest < 1 or rate < 1 or months < 1:
            continue
        
        final_value = "Cressimento mensal do investimento:"
        for month in range(1, months + 1):
            final_value += f"\n{month}º Mês: R$ {invest * (1 + rate / 100) ** month:_.2f}"
        
        final_value = final_value.replace(".", ",").replace("_", ".")
    except ValueError:
        continue
    
    break


print(f"\n{final_value}\n")
