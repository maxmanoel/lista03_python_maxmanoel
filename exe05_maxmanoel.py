#- Pergunte ao usuário se está chovendo e converta sua resposta em minúsculas para que não importe em que caso ele digite. Se ele responder "sim", pergunte se está ventando. 
# Se ele responder "sim" a esta segunda pergunta, exiba a resposta "Está ventando muito para um guarda-chuva", caso contrário, exiba a mensagem "Pegue um guarda-chuva".
#  Se ele não respondera sim à primeira pergunta, mostre a resposta "Aproveite o seu dia".

chuva = str(input("Esta chovendo agora : "))
print(chuva.lower())
if "sim" in chuva:
    vento = str(input("Esta ventando ? "))
if "sim" in vento:
    print ("Está ventando muito para um guarda-chuva")
    print ("MAX MANOEL")
elif "nao" in vento:
    print ("Pegue um guarda-chuva")
    print ("MAX MANOEL")
else:
    print ("Aproveite seu dia")
    print("MAX MANOEL")