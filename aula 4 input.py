faturamento = input('qual o faturamento este mes?')
custo = input('qual o custo este mes?')

if faturamento:
    lucro = int(faturamento) - int(custo)
    print('o lucro da loja foi de {} reais'.format(lucro))
