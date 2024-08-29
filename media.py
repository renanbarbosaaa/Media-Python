import os
os.system('cls')


n1 = n2 = media = 0.0

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))

media = (n1+n2)/2

if(media >= 7):
    print('Aluno aprovado!')
    print('Parabéns!')

else:
    print('Aluno reprovado')

print('O aluno tirou nota:', media)             