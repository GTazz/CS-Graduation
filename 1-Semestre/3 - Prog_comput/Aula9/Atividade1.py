from os import system as cmd


def print_title(prjct_title: str, style: str="-x-=") -> None:
    cmd("cls")  # Limpa a tela do terminal
    t_lines = f"\033[1;34m{style * int(len(prjct_title) / len(style)+1)}"[:7+len(prjct_title)] + "\033[m" # cria as linhas do tamanho do título
    print(f"{t_lines}\n\033[1;33m{prjct_title.upper()}\n{t_lines}\n") # imprime o título junto as linhas


print_title("Funções de manipulação de string")


TEST_STR = "Manipulação de string"

print(TEST_STR.split()) # Divide a string para po formato de Array

print(TEST_STR.find("string")) # Encontra onde inicia o índice da palavra "string"
print(TEST_STR.find("de")) # Encontra onde inicia o índice da palavra "de"

print(TEST_STR.replace("de", "com")) # Substitui uma palavra por outra dentro de uma string

print(TEST_STR.upper()) # Deixa o texto completamente em maiúsculo
print(TEST_STR.lower()) # Deixa o texto completamente em minúsculo

print(TEST_STR.split("de")) # Divide a string para po formato de Array





print()