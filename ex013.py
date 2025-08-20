import random
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
res = [a1,a2,a3]
random.shuffle(res)
print('A sequencia ficou {}'.format(res))