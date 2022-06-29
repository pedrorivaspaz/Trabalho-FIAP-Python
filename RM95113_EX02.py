segunda_feira = int(input("Informe o número de votos que segunda-feira obteve "))
terca_feira = int(input("Informe o número de votos que terça-feira obteve "))
quarta_feira = int(input("Informe o número de votos que quarta-feira obteve "))
quinta_feira = int(input("Informe o número de votos que quinta-feira obteve "))
sexta_feira = int(input("Informe o número de votos que sexta-feira obteve "))

segunda_feira == 0
terca_feira == 0
quarta_feira == 0
quinta_feira == 0
sexta_feira == 0
#teste lógico
if segunda_feira > terca_feira  and  segunda_feira > quarta_feira and segunda_feira > quinta_feira and segunda_feira > sexta_feira :
    print("O dia escolhido foi segunda-feira")
elif terca_feira > segunda_feira and terca_feira > quarta_feira and terca_feira > quinta_feira and terca_feira > sexta_feira :
    print("O dia escolhido foi terça-feira")
elif quarta_feira > segunda_feira and quarta_feira > terca_feira and quarta_feira > quinta_feira and quarta_feira > sexta_feira :
    print("O dia escolhido foi quarta-feira")
elif quinta_feira > segunda_feira and quinta_feira > terca_feira and quinta_feira > quarta_feira and quinta_feira > sexta_feira :
    print("O dia escolhido foi quinta-feira")
elif sexta_feira > segunda_feira and sexta_feira > terca_feira and sexta_feira > quarta_feira and sexta_feira > quinta_feira :
    print("O dia escolhido foi sexta-feira")
else:
    print("Houve empate")
