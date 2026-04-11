# Aprimore o desafio anterior,mostrando no final:
# A)A soma de todos os valores pares digitados
# B)A soma dos valores da terceira coluna
# C)O maior valor da segunda linha

matriz=[[0,0,0],[0,0,0],[0,0,0]]
vp=0
vtc=0
for c in range(3):
    for l in range(3):
        matriz[c][l]=int(input(f'Digite o valor de: [{c},{l}] '))
print('\033[36m-=-'*30)
print('\033[m')
for linha in matriz:
    vtc=vtc+linha[2]
    for valor in linha:
        print(f'[{valor:^7}]',end=' ')
        if valor %2==0:
            vp=vp+valor
    print()
print('\033[36m-=-'*30)
print('\033[m')
maior=matriz[1][0]
for c in matriz[1]:
    if c>maior:
        maior=c
print(f'A soma dos valores pares é de {vp}')
print(f'A soma dos valores da terceira coluna é de {vtc}')
print(f'O Maior valor da segunda linha é {maior}')

