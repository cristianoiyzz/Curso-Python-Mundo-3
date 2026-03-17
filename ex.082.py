# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso,Crie duas listas extras que vão conter apenas os valores pates e os valores impares digitados,respectivamente
# Ao final mostre o resultado das três listas geradas

valores=[]
par=[]
impar=[]
parf=''
imparf=''
while True:
    while True:
        numt=str(input('Digite o valor: '))
        if numt.isnumeric():
            num=int(numt)
            valores.append(num)
            break
        else:
            print('\033[31mDigite Apenas Números!\033[m')
    if num%2 == 0:
        parf='sim'
        par.append(num)
    if num%2 == 1:
        imparf='sim'
        impar.append(num)
    while True:
        continuar=str(input('Deseja continuar ? [S/N]: ')).upper().strip()[0]
        if continuar in 'SN':
            break
        else:
            print('\033[31mDigite Apenas [S/N]!\033[m')
    if continuar=='N':
        break
print(f'A lista completa é: {valores}')
if parf=='sim':
    print(f'Os Valores Pares são: {par}')
if imparf=='sim':
    print(f'Os valores impares são: {impar}')
