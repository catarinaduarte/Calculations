# - Exercício: script (calculos1.py) que pede número ao utilizador e que exibe:
#     . dobro
#     . triplo
#     . quadrado
#     . cubo
#     . resultado de 2.5x + 10, onde x é o número pedido ao utilizador

import sys
from decimal import Decimal as dec

# sys.argv é uma lista com todos os argumentos 
# passados na linha de comandos ao interpretador,
# ou seja, inclui também o nome do script
#
#       $ python3 o_mey_script.py 90 alberto
#
#           sys.argv -> ['o_meu_script.py', '90', 'alberto']

num = dec(sys.argv[1])

print(f"Dobro     : {2*num:^10.2f}")
print(f"Triplo    : {3*num:^10.2f}")
print(f"Quadrado  : {num * num:^10.2f}")         # ou num ** 2
print(f"Cubo      : {num * num * num:^10.2f}")   # ou num ** 3
print(f"2.5x + 10 : {dec('2.5') * num + 10:^10.2f}")


