# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.Depois disso mostre:
# a listagem de números gerados e também indique o menor e o maior valor que estão na tupla
from random import randint
maior=0
menor=0
for c in range (0,5):
    num = (randint(0, 10))
    print(num,end=' ')
    if c == 0:
        maior=num
        menor=num
    if num>maior:
        maior=num
    if num<menor:
        menor=num
print(f'\nO Maior Número sorteado foi: {maior}\nO Menor Número sorteado foi: {menor}')
#Modo mais simples
# num=(randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
# print(num)
# print(f'O maior valor digitado foi {max(num)}')
# print(f'O menor valor digitado foi {min(num)}')