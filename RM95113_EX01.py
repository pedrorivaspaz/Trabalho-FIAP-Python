#Solicitando os dados
tipo_de_assinatura= input("Por favor informe sua assinatura: BASIC,SILVER,GOLD,PLATINUM ")
faturamento_anual= float(input("Informe o seu faturamento anual "))
#teste lógico
if tipo_de_assinatura. upper() == "BASIC" :
    valor_a_ser_pago = faturamento_anual * 0.3
elif tipo_de_assinatura. upper() == "SILVER" :
    valor_a_ser_pago = faturamento_anual * 0.2
elif tipo_de_assinatura. upper() == "GOLD" :
    valor_a_ser_pago = faturamento_anual * 0.1
elif tipo_de_assinatura. upper() == "PLATINUM" :
    valor_a_ser_pago = faturamento_anual * 0.05
else:
    print('Assinatura inexistente')
print("O valor a ser pago é de R${}.".format( valor_a_ser_pago))
