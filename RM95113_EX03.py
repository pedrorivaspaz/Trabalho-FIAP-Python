p = 0
for x in range(2,51,2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
    pares = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}".format(x)))
    p = p + pares

i = 0
for x in range(1,51,2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES")
    impares = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}".format(x)))
    i = i + impares

p = p / 25
i = i / 25
#teste lógico
if p > i :
    print( "A média da turma par é de: {} e da número ímpar é de: {}, sendo assim a média dos alunos pares é maior que as de número impar".format(p, i))
elif i > p :
    print("A média da turma ímpar é de: {} e da número par é de: {}, sendo assim a média dos alunos impar é maior que as de número par".format(i, p))
elif p == i :
    print("A média da turma par é de: {} e da número ímpar é de: {}, sendo assim a média dos alunos são iguais".format(p, i))


