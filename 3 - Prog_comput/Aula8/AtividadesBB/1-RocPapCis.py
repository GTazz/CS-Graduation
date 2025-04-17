from os import system as cmd
from random import choice
from difflib import get_close_matches


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas

def close_to(str_input, str_list):
    closer = get_close_matches(str_input, str_list, n=1, cutoff=0.6)
    return closer[0] if closer else None


SYMBOLS = {
    "pedra": "✊",
    "papel": "✋",
    "tesoura": "✌️"
}

comp_symbol = choice(list(SYMBOLS.keys()))

symbol = None
while symbol == None:
    print_title("Pedra | papel | tesoura", "-[0]-=-[1]-=")
    symbol = close_to(input("Escolha entre pedra, papel ou tesoura: ").strip().lower(), list(SYMBOLS.keys()))

print(f"\nVocê escolheu: {SYMBOLS[symbol]}")
print(f"O computador escolheu: {SYMBOLS[comp_symbol]}\n")
print("\033[1;33mEMPATE!\033[m\n" if symbol == comp_symbol else 
      "\033[1;32mVOCÊ VENCEU!\033[m\n" if (symbol == "pedra" and comp_symbol == "tesoura") or (symbol == "papel" and comp_symbol == "pedra") or (symbol == "tesoura" and comp_symbol == "papel") else 
      "\033[1;31mVOCÊ PERDEU!\033[m\n"
      )
