# coding: utf-8

#Iterando listas em Python
# o código abaixo não soma 1000 a cada indice
# lista_nums = [100,200,300,400]
# for item in lista_nums:
#     item += 1000
# print(lista_nums)

# lista_nums = [100,200,300,400,500,600,700,800]
# for item in range(len(lista_nums)):
#     lista_nums[item] += 1000
# print(lista_nums)

# função de nome enumerate
lista_nums = [100,200,300,400,500,600,700,800]
for idx, item in enumerate(lista_nums):
    lista_nums[idx] += 1000
print(lista_nums)