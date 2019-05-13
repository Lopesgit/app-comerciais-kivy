# coding: utf-8

#TRATAMENTO DE EXCEÇÕES MÚLTIPLAS

def erro(x):
    try:
        eval(x)
    except (TypeError, NameError):
        print("TypeError ocorreu ou então, NameError")
    except ValueError:
        print("ValueError")
    except ZeroDivisionError:
        print("ZeroDivisionError")


#TypeError
erro("int+int")
#NameError
erro("a")
#ValueError
erro("int('a')")
#ZeroDivisionError
erro("5/0")

