minutos = int(input("Informe os minutos que o seu computador está marcando: "))
minutos_fatorial = 1
while (minutos > 0):
    minutos_fatorial = minutos_fatorial * minutos
    minutos = minutos - 1
print("Senha para o desbloqueio é: LIBERDADE",minutos_fatorial)


