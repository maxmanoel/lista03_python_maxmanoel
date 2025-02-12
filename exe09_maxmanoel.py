#Escreva um programa que faça o cálculo do imposto de renda 2025. Consulte a tabela no site da Receita federal.
n1 = float(input("Digite seu salario: "))
if(n1> 2.259,21 and n1<2.826,65):
    conta =n1 * 0.075
    print("voce vai pagar " ,conta ,"de imposto")
if(n1>2.826,66 and n1<3.751.05):
    conta = n1 * 0.15
    print("voce vai pagar " ,conta ,"de imposto")
    if(n1> 3.751,06 and 4.664,68 ):
        conta  = n1 * 0,225
        print("voce vai pagar " ,conta ,"de imposto")
    if(n1>4.664,68):
        conta = n1 * 0,275
        print("voce vai pagar " ,conta ,"de imposto")

    