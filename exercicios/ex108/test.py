# FORMATANDO MOEDA EM PYTHON

from ex108 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de R$ {moeda.moeda(p)} é R${moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos R${moeda.moeda(moeda.aumentar(p, 10))}')
