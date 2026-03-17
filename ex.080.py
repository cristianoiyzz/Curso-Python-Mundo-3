# Crie um programa onde o usuário possa digitar cinco valores númericos e cadastre-os em uma lista,já na posição correta de inserção(sem usar o sort).
# No final,mostre a lista ordenada na tela.

valores=[]

for c in range(1,6):
    num=int(input(f'Digite o {c} °Valor: '))
    if c==1 or num>valores[-1]:
        print('Adicionamos esse valor no final da lista...')
        valores.append(num)
    else:
        pos=0
        while pos < len(valores): #pos só vai ser igual a len(valores) caso tenha percorrido todos os números então funciona como uma especie de scanner
            if num<=valores[pos]: #vai encontrar a  sua posição,obs:se caiu aqui no else ele precisa acha sua posição
                print(f'Adicionamos na posição {pos}')
                valores.insert(pos,num)
                break
            pos+=1 #vai andando um por e vai alterando a analise da linha 14
print(valores)