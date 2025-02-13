#Pergunte a idade do usuário. Se tiver 16 anos ou mais, exiba a mensagem "Você pode votar", 
# se tiver 18 anos, exiba a mensagem "Você pode aprender a dirigir", se tiver 14 anos, exiba a mensagem "Você pode comprar um bilhete de loteria", 
# se tiver menos de 14 anos, exiba a mensagem "Você pode fazer doces ou travessuras".

n1 = int(input("Digite sua idade: "))

if(n1>=18 ):
    print("voce pode dirigir")
else:
    if(n1>=16):
         print("voce pode votar")
    print("MAX MANOEL")     
if(n1<=14):
        print("voce pode comprar um bilhete de loteria")
        print("MAX MANOEL")
else:
     print("Voce pode fazer doces ou travessuras")