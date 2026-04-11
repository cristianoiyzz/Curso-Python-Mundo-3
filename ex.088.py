# Faça um programa que ajude um jogador da mega sena a criar palpites.
# o programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,cadastrando tudo em uma lista composta
from random import randint
from time import sleep
valores=list()
jogos=list()
cont=0
contador=0
print('\033[36m-=-'*10,'\033[m')
print('\033[m      MEGA SENA      ')
print('\033[36m-=-'*10,'\033[m')
while True:
    qntdt=str(input('Quantos jogos você quer que eu sorteie? '))
    if qntdt.isnumeric():
        qntd=int(qntdt)
        break
    else:
        print('\033[31mErro Digite Apenas Números Inteiros!\033[m')
while qntd>cont:
    while len(valores)<6:
        num=randint(0,60)
        if num not in valores and len(valores)<6:
                valores.append(num)
    cont+=1
    valores.sort()
    jogos.append(valores[:])
    valores.clear()
print('-=-'*2,f'\033[36mSORTEANDO {cont} JOGOS\033[m','-=-'*2)
for linha in jogos:
    contador+=1
    print(f'Jogo {contador}  ',end='')
    for valor in linha:
        print(f'{valor:^2}',end='  ')
    sleep(1)
    print()







