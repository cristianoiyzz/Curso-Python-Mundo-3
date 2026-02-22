#Crie um programa que tenha uma tupla totalmente prrenchida por uma contagem por extenso,de zero até vinte. Seu Programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso
lanche=('zero','um','dois','Três','quarto','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quartorze','quinze','desseseis','dezesete','dezoito','dezenove','vinte')
while True:
    numt=str(input('Digite o valor que deseja ver por extenso de 0 a 20: '))
    if numt.isnumeric():
        num=int(numt)
        if num<=20 and num>=0:
            break
print(f'Você digitou o número {lanche[num]}')