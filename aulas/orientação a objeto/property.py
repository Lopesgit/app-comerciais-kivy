# coding: utf-8

#PROPERTY

class A:
    def __init__(self):
        self._var = 0
    def _get_var(self):
        print("o valor está sendo lido")
        return self._var
    def _set_var(self, x):
        print("o valor está sendo escrito")
        self._var = x

    var = property(fget=_get_var, fset=_set_var)

a = A()
a.var = 10
print(a.var)
