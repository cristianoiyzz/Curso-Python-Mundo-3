#Crie um programa que tenha uma tupla com várias palavras(não usar acentos).Depois disso ,você deve mostrar,para cada palavra,quais são as suas vogais

palavras='aprender','programar','linguagem','python','curso','gratis','estudar','praticar','trabalhar','mercado','programador','futuro'
for c in palavras:
    print(f'\nNa Palavra {c.upper()} temos:',end='')
    for letra in c:
        if letra in 'aeiou':
            print(letra,end=' ')
