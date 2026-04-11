# Crie um programa que leia nome e duas notas de vários 2 alunos e guarde tudo em uma lista composta.
# No final,mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente
dados=[]
opc=0
while True:
    while True:
        nome=str(input('Nome: ')).strip()
        if nome.replace(' ','').isalpha():
            break
        else:
            print('\033[31mDigite Apenas Caracteres\033[m')
    while True:
        n1t=str(input('Nota 1: '))
        if n1t.replace('.','',1).isnumeric():
            n1=float(n1t)
            break
        else:
            print('\033[31mDigite Apenas Números\033[m')
    while True:
        n2t=str(input('Nota 2: '))
        if n2t.replace('.','',1).isnumeric():
            n2=float(n2t)
            break
        else:
            print('\033[31mDigite Apenas Números\033[m')
    media=(n1+n2)/2
    dados.append([nome, [n1, n2], media])
    while True:
        continuar=str(input('Deseja continuar? [S/N]: ')).upper()
        if continuar in ['S','N']:
            break
        else:
            print('\033[31mDigite Apenas S ou N\033[m')
    if continuar == 'N':
        break
print('No.  NOME    MÉDIA')
print('-'*30)
for i,aluno in enumerate(dados):
    print(f'{i}    {aluno[0]:<7}{aluno[2]:>5}')
print('-'*30)

while opc !=999:
    opc=int(input('Mostrar Notas de Qual Aluno? (999 interrompe): '))
    if opc == 999:
        break
    if opc>=len(dados):
        print('Essa pessoa não está listada.')
    else:
        print(f'As notas de {dados[opc][0]} são {dados[opc][1]}')
