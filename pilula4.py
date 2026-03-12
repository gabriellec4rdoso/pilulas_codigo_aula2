import statistics as st
lote1 = int(input('produção lote1:'))
lote2 = int(input('produção lote2:'))
lote3 = int(input('produção lote3:'))
media = st.mean((lote1,lote2,lote3))
desvio = st.stdev ((lote1,lote2,lote3))
print(f'média:{media:.2f}')
print(f'desvio padrão: {desvio:.2f}')