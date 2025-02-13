#Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
#  Você deve poder calcular a soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada. (usar ELIF)
print("soma (+), subtração (-), multiplicação (*) e divisão (/)")
n1 = float(input("Digite primeiro numero: "))
n2= float(input("Digite segundo numero: "))
calc = (input("Digite a operação que voce eseja utilizar: "))
if "+" in calc:
    print("A soma e" , n1+n2)
    print("MAX MANOEL")
elif "-" in calc:
    print("A subtração e" , n1-n2)
    print("MAX MANOEL")
elif "*" in calc:
    print("A multiplicação" , n1*n2)
    print("MAX MANOEL")
elif"/" in calc:
    print("A divisão" , n1/n2)
    print("MAX MANOEL")

