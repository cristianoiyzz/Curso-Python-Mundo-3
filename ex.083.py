# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

pilha=[]
expressao=str(input('Digite a expressão: '))
for c in expressao:
    if c == '(':
        pilha.append(expressao)
    elif c == ')':
        if len (pilha) > 0 :
            pilha.pop()
        else:
            pilha.append(expressao)
            break
if len (pilha) == 0:
    print('a expressão está valída! ')
else:
    print('a expressão não está valída! ')



