import datetime
#entrada
data_compra = input('digite a data da compra d/m/aaaa:' )
meses = int(input('prazo da garantia:'))
#processamento
data_inicial = datetime.datetime.strptime(data_compra, '%d/%m/%Y')
data_final = data_inicial + datetime.timedelta(days=meses * 30)
#saida
print(f'garantia válida até {data_final.strftime('%d/%m/%Y')}')
print(f'dia da semana: {data_final.strftime('%A')}')