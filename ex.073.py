#Crie uma tupla preenchida com os 20 primeiros colocados do camepeonato brasileiro de futebol. na ordem de colocação.Depois mostre:
# A)Apemas os 5 primeiros colocados
# B)Os últimos 4 colocados da tabela
# C)uma lista com os times em ordem alfabética
# D)Em que posição na tabela está o time da chapecoense
times=('Palmeiras','São Paulo','Fluminense','Bahia','Corinthians','Athletico-PR','Bragantino','Chapecoense','Mirassol','Coritiba','Flamengo','Botafogo','Grêmio','EC Vitória','Atlético-MG','Remo','Vasco Da Gama','Santos','Internacional','Cruzeiro')
print('''
\033[36m==========================
======\033[mBRASILEIRÃO\033[36m=========\033[m''')
print('Todos Os Times:')
print(f'{times}')
print('Primeiros 5 colocados:')
print(f'{times[0:5]}')
print('Os Ùltimos 4 colocados:')
print(f'{times[16:]}')
print('Os times em ordem alfabetica:')
print(f'{sorted(times)}')
print(f'Em que posição na tabela está o time da chapecoense:)')
print(f'Chapecoense está na posição: {times.index("Chapecoense")+1}')
