# JOGO DA ADIVINHAÇAO V1.0

from random import randint
from time import sleep
computador = randint(0, 5) # faz o computador "pensar"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # jogador tenta advinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me venceu!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
