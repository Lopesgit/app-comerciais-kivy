# coding: utf-8

# Argumentos posicionais e argumentos nomeados


def dados_pessoais(nome, sobrenome, idade, sexo):
    print("Nome: {}\nSobrenome: {}\nIdade: {}\nSexo: {}"
          .format(nome, sobrenome, idade, sexo))

# dados_pessoais("Renê", "Lopes", 35, True)
dados_pessoais(idade=35, sexo=True, sobrenome="Barros", nome="Renê")

