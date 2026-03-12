import random
#entradas
cotacao = float(input('cotacao atual do dólar'))
#processamento
variacao = random.uniform(-0.015, 0.015)
nova_cotacao = cotacao * (1 + variacao)
#saida
print(f'variação simulada: {variacao:.3%}')
print(f'nova cotação R${nova_cotacao:.4f}')