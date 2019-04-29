# coding: utf-8

# Funções aninhadas


def func():
    print("func")

    def func_interna():
        print("func_interna")

    func_interna()


func()