# coding: utf-8

# a = 10
# b = 25
# c = 66
#
# x = int(input("Digite um número: "))
#
# # if(x == a or x == b or x == c):
# # if(x in [10, 25, 66]):
# if x in [a, b, c]:
#     print("Está contido.")
# else:
#     print("NÃO está contido.")

#---------------------------------------

cores = ["azul", "amarelo", "vermelho", "branco"]

while True:
    cor = input("Digite o nome de uma cor ou então, "
                  "0 para siar do programa: ")

    if cor == "0":
        break
    if cor in cores:
        print("Essa cor está contida!")
    else:
        print("Essa cor NÃO está contida!")
    print()

