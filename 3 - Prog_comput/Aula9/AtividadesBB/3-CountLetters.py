from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


def analise_letters(str_target: str) -> str:
    formatted_str = ""
    repeated = ""
    for char in str_target:
        if char in repeated:
            continue
        repeated += char
        num_char = str_target.count(char)
        if num_char > 0:
            formatted_str += str_target.replace(char, f"\033[1;42;30m{char}\033[m")
            formatted_str += f" | Quant. de \"{char}\": {num_char}\n"
    
    return formatted_str.strip("\n")


print_title("Contando ocorrências em string", "{0}<1>") 

format_str = analise_letters(input("Digite uma string: ").upper()) 

print(f"\n{format_str}\n") 
