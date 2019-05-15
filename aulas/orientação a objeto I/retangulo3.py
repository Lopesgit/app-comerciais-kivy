# coding: utf-8

class Retangulo:

    def __init__(self, largura, altura):
        self.l = largura
        self.a = altura

    def area(self):
        return self.a * self.l

r = Retangulo(7, 5)
print(r.area())