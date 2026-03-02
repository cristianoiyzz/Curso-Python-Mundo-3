#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
lanche = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
while True:
    numt=str(input('Digite o número que deseja ver por entexso: '))
    if numt.isnumeric():
        num=int(numt)
        if 0 <= num <=20:
            print(f'Você digitou o número {lanche[num]}')
        else:
            print('\033[31mDigite Apenas números de [0 a 20]\033[m')
            continue
    else:
        print('\033[31mErro  digite apenas números nesse campo\033[m')
        continue
    while True:
        continuar=str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
        if continuar in 'SN':
            break
        else:
            print('\033[31mDigite Apenas [S/N]\033[m')
    if continuar=='N':
        break
print('Programa Encerrado')