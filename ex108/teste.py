import moeda

p = float(input('Digite o preco: R$ '))
print(f'A metade de R$ {moeda.moeda(p)} é {moeda.moeda(p)}')
print(f'O dobro de R$ {moeda.moeda(p)} é {moeda.moeda(p)}')
print(f'Aumentando 10%, temos {moeda.moeda(p)}')

