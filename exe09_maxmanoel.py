#Escreva um programa que faça o cálculo do imposto de renda 2025. Consulte a tabela no site da Receita federal.
n1 = float(input("Digite seu salario: "))
if(n1> 2259.21 and n1<2826.65):
    conta =n1 * 0.075
    print("voce vai pagar R$" ,conta ,"de imposto o que sobrou do salario" , n1 - conta )
    print("MAX MANOEL")

if(n1>2826.66 and n1<3.7515):
    conta = n1 * 0.15
    print("voce vai pagar R$" ,conta ,"de imposto o que sobrou do salario" , n1 - conta )
    print("MAX MANOEL")

    if(n1> 37516 and 4664.68 ):
        conta  = n1 * 0,225
        print("voce vai pagar R$" ,conta ,"de imposto o que sobrou do salario" , n1 - conta )
        print("MAX MANOEL")

    if(n1>4664.68):
        conta = n1 * 0,275
        print("voce vai pagar R$" ,conta ,"de imposto o que sobrou do salario" , n1 - conta )
        print("MAX MANOEL")

    