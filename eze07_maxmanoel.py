#Peça ao usuário para inserir 1, 2 ou 3. Se ele inserir um 1, exiba a mensagem "Obrigado", se ele inserir um 2, exiba "Muito bem", se ele inserir um 3,
#  exiba "Correto". Se ele inserir qualquer outra coisa, exiba "Mensagem de erro".

n1 = int(input("Digite um numero: "))

if(n1==1 ):
    print("Obrigado")
elif(n1==2):
    print("Muito bem")    
elif(n1==3):
    print("correto")
else:
     print("mensagem de erro")
print("MAX MANOEL")