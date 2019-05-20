# coding: utf-8

#PROPERTY - DECORATORS

class A:
    def __init__(self):
        self._var = 0
    @property
    def var(self):
        print("o valor está sendo lido")
        return self._var
    @var.setter
    def var(self, x):
        print("o valor está sendo escrito")
        self._var = x

a = A()
a.var = 10
t = a.var
print(t)
