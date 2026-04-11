# Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final,mostre:
#
# A) Quantas Pessoas foram cadastradas
# B) Uma listagem com as pessoas mais pesadas.
# C)uma listagem com as pessoas mais leves.

dado=list()
pessoas=list()
totp=0
maior=0
menor=0
maximo=list()
minimo=list()
while True:
    while True:
        nome=(str(input('Nome: '))).strip()
        if nome.replace(' ','').isalpha():
            dado.append(nome)
            break
        else:
            print('\033[31mDigite Apenas Caracteres\033[m')
    while True:
        pesot=str(input('Peso: '))
        if pesot.replace('.','',1).isnumeric():
            peso=float(pesot)
            dado.append(peso)
            break
        else:
            print('\033[31mErro Digite Apenas Números.\033[m ')

    if totp==0:
        menor=peso
        maior=peso
    else:
        if peso <= menor:
                menor=peso
        if peso >= maior:
                maior=peso

    pessoas.append(dado[:])
    dado.clear()
    totp += 1
    while True:
        continuar=str(input('Deseja continuar?[S/N] ')).upper()
        if continuar in ['S','N']:
            break
        else:
            print('\033[31mDigite Apenas S ou N!\033[m')
    if continuar=='N':
        break
print(f'Foram cadastradas ao todo {totp} Pessoas!')
for c in pessoas:
    if c[1]==maior:
        maximo.append(c[0])
    if c[1]==menor:
        minimo.append(c[0])
print(f'Com {maior} Os mais pesados foram: {maximo}')
print(f'Com {menor} Os mais leves foram: {minimo}')


