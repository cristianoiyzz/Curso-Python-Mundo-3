#Crie um programa que vai ler vários números e colocar em uma lista,Depois Disso Mostre:
# A)Quantos números foram digitados
# B)A lista de valores ordenada de forma descrescente
# C)Se o valor 5 foi digitado e está ou não na lista.
continuar=''
valores=[]
c=1
while True:
    while True:
        numt=str(input(f'Digite o {c}° '))
        if numt.isnumeric():
            num=int(numt)
            c+=1
            valores.append(num)
            break
        else:
            print('\033[31mDigite Apenas Números\033[m')
    while True:
        continuar=str(input('Deseja Continuar?[S/N]: ')).upper().strip()[0]
        if continuar in 'SN':
            break
        else:
            print('\033[31mDigite Apenas [S/N]!\033[m')
    if continuar=='N':
        break
valores.sort(reverse=True)
print(f'O Total De Números digitados foram: {c-1}')
print(f'A lista de valores ordenada em forma descrescente é: {valores}')
if 5 in valores:
    print(f'O Valor 5 está adicionado na lista na posição {valores.index(5)+1}')
else:
    print('O valor 5 não está presente na lista')