# Leia o preço de um produto e mostre seu novo preço com 5% de desconto
# TOTAL = 100
# X     = 5
# x * 100 = total * 5 --> x * 100 = total_mult --> x = total_mult / 100

produto = float(input('Preço do produto: R$'))
desconto = (produto * 5) / 100
produto = produto - desconto 

print(f'O produto receberá um desconto de 5% (R${desconto:.2f}) e agora seu valor é de R${produto:.2f}!')
