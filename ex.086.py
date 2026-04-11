# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final,mostre a matriz na tela,com a formatação correta.

matriz=[[0,0,0],[0,0,0],[0,0,0]]
for l in range(3):
    for c in range(3):
        matriz[l][c]=int(input(f'Digite o valor [{l},{c}]: '))
for linha in matriz:
    for valor in linha:
        print(f'[{valor:^7}]',end=' ')
    print()