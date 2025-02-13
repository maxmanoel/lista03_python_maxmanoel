#Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. 
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.

n1 = int(input("Digite a distancia que voce ira percorrer: "))
if(n1<200):
    conta = n1 *0.50
    print("voce pagara o total de R$"  , conta, "nessa viagem km", n1)
if(n1>200):
    conta = n1 * 0.45
    print("voce pagara o total de R$"  , conta, "nessa viagem km", n1)
print("MAX MANOEL")
