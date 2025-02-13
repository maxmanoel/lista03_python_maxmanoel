#Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, de 15%.
n1 = float(input("Digite seu salario: "))
if(n1<1250.00):
    conta = n1 * 0.15
    print("Voce recebeu um aumento de R$" , n1 + conta)
    print("MAX MANOEL")
else:
    conta = n1 * 0.10
    print("Voce recebeu um aumento de R$" , n1 + conta)
    print("MAX MANOEL")

