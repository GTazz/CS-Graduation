from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("MAnipulação de string", "[0]-=-[1]-=-")

txt_input = input("Digite algo: ")
char0 = txt_input[0] # B

SIZE = len(txt_input) # 6

print(f"""
{SIZE} é a quantidade de carácteres presentes no texto \"{txt_input}\".
\"{txt_input}\" ao contrário é: \"{txt_input[::-1]}\"."
""")

