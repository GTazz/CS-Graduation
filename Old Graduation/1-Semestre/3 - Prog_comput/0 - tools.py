from os import system, mkdir

def func1():
    print("func1")


def func2():
    print("func2")


if __name__ == "__main__":
    dict_object = {1: func1, 2: func2}
    call_function = 0
    while 1 > call_function or call_function > 2 or str(type(call_function)) == "<class 'str'>":
        call_function = int(input(
"""
Selecione a função desejada:

[1] func1
[2] func2

"""))

    dict_object[call_function]()
    