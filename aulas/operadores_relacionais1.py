idade = int(input("informe a sua idade:"))

if(idade<=0):
    print("A sua idade não pode ser 0 ou menor do que 0!")
elif(idade>150):
    print("A sua idade não pode ser superior a 150 anos!")
elif(idade<18):
    print("Você precisa ter mais que 18 anos!")