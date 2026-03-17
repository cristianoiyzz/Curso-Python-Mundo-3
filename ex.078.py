# faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final,mostre qual foi o maior valor digitado e as suas respectivas posições na lista.

valores=[]
for c in range (0,5):
    while True:
        numt=str(input(f'Digite Um Valor inteiro para a posição {c}: '))
        if numt.isnumeric():
            num=int(numt)
            valores.append(num)
            break
maior=max(valores)
menor=min(valores)
print(f'Você digitou os valores {valores}')
print(f'O Maior Número Encontrado foi: {maior} nas posições ',end='')
for c,v in enumerate(valores):
    if v==maior:
        print(f'[{c}]',end='..')
print(f'\nO Menor Número Encontrado foi: {menor} nas posições ',end='')
for c,v in enumerate(valores):
    if v==menor:
        print(f'[{c}]',end='..')