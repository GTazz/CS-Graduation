from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("Financiamento com juros")

value = float(input("Digite o valor do financiamento: R$"))
qntt_fee = int(input("Digite a quantidade de parcelas: "))

if qntt_fee == 1:
    invoice_fee = .0
elif qntt_fee == 2:
    invoice_fee = .03
elif qntt_fee <= 4:
    invoice_fee = .07
elif qntt_fee <= 6:
    invoice_fee = .09
elif qntt_fee <= 8:
    invoice_fee = .12

fee = (value + value * invoice_fee) / qntt_fee

print(f"\nCom {invoice_fee*100:.0f}% de juros, valor de cada parcela será de R${fee:.2f}.\n")
