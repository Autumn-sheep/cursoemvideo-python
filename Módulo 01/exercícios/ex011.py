# Leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considerando - US$1.00 = R$3,27
saldo = float(input('SALDO: R$'))
dolar = saldo / 3.27
print(f'Você pode comprar US${dolar:.2f}.')
