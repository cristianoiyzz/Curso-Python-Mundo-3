# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.Caso o número já exista lá dentro,ele não será adicionado.
# No final,serão exibidos todos os valores únicos digitados,em ordem crescente.

valores=list()
continuar=''
while True:
    while True:
        numt=str(input('Digite um número: '))
        if numt.isnumeric():
            num=int(numt)
            if num in valores:
                print('valor duplicado não será adicionado')
            else:
                valores.append(num)
            break
    while True:
        continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
        if continuar in 'SN':
            break
        else:
            print('\033[31mErro,Digite Apenas [S/N]\033[m ')
    if continuar=='N':
        break
valores.sort()
print(f'Valores Digitados Em Ordem {valores}')
