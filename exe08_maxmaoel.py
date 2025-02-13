#Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. 
# Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

n1 = int(input("Digite a velocidade do carro: "))
if(n1>80):
    conta = (n1 - 80)*5
    print("voce foi multado por utrapasar o limite de 80 km")
    print("voce passou a km"  , n1, "os 80 km/hr e voce tera que pagar uma multa de ", conta)
    print("MAX MANOEL")
else:
    print("Parabens voce esta no limite certo de velocicade ")
    print("MAX MANOEL")
