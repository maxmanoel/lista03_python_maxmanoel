#Peça ao usuário para inserir sua cor favorita. Se ele digitar "vermelho", "VERMELHO" ou "Vermelho" exibem a mensagem "Eu também gosto de vermelho", 
# caso contrário, exibem a mensagem "Eu não gosto de [cor], eu prefiro vermelho".
cor = str(input("Digite sua cor favorita : "))
cor1=cor.title()
if (cor1 == "Vermelho"):
    print ("Eu também gosto de vermelho")
    print ("MAX MANOEL")
else:
    print ("Eu não gosto de ",cor,",eu prefiro vermelho")
    print ("MAX MANOEL")