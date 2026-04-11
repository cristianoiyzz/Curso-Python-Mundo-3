# Crie um programa onde o usuário possa digita sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final,mostre os valores pares e ímpares em ordem crescente
valores=[[], []]
for c in range(1,8):
    num=int(input(f'Digite o {c}° valor: '))
    if num%2==0:
        valores[0].append(num)
    else:
        valores[1].append(num)
        valores[33].append(num)
valores[0].sort()
valores[1].sort()
if len(valores[0]) >=1:
    print(f'Esses são os valores pares {valores[0]}')
else:
    print('Você não digitou valores pares')
if len(valores[1]) >=1:
    print(f'Esses são os valores ímpares {valores[1]}')
else:
    print('Você não digitou  valores ímpares')