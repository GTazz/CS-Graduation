from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("Cálculo de lucro")


product_name = input("Digite o nome do produto: ")
purchase_price = float(input("Digite o valor da compra: R$"))

if purchase_price < 0:
    print("\nValor inválido!!\n")
else:
    if purchase_price < 10:
        selling_price = purchase_price * 1.70
    elif 10 <= purchase_price < 30:
        selling_price = purchase_price * 1.50
    elif 30 <= purchase_price < 50:
        selling_price = purchase_price * 1.40
    else:
        selling_price = purchase_price * 1.30

    print(f"\nProduto: {product_name}")
    print(f"Valor de venda: R${selling_price:.2f}\n")
