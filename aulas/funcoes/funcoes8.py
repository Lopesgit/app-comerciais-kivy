# coding: utf-8

# Desempacotamento


def pessoa(nome, sobrenome, idade):
    print(nome)
    print(sobrenome)
    print(idade)


# tupla = "eXcript", "Brasil", 20
#pessoa(tupla[0], tupla[1], tupla[2])
# pessoa(*tupla)

# lista = ["eXcript", "Brasil", 20]
# pessoa(*lista)

d = {"sobrenome": "Brasil", "idade": 20, "nome": "eXcript",}
pessoa(**d)