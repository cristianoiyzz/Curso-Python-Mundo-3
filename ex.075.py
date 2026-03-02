# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final,mostre:
# A)Quantas Vezes apareceu o valor 9
# B)Em que posição foi digitado o primeiro valor 3
# C)Quais foram os números pares
c=0
num=tuple(int(input('Digite um valor: ')) for c in range(0,4))
print(f'O 9 Apareceu {num.count(9)} Vezes')
# if num.count(3)>0:
#     print(f'O valor 3 apareceu primeiro na posição [{num.index(3)}]')
# else:
#     print('Você Não Digitou Nenhum valor corresponente a 3')
print(f'O valor 3 apareceu primeiro na posição [{num.index(3)+1}]'if num.count(3)>0 else 'Você Não Digitou Nenhum valor corresponente a 3')
print(f'Você digitou os seguintes números pares: ',end='')
for c in num:
    if c%2==0:
        print(c,end='.. ')






