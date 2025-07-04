# Leia um valor em metros e mostre ele em centímetros e milímetros
metros = int(input('Digite um valor em metros:\n> '))

centimetros = metros * 100
milimetros = metros * 1000
print(f'{metros} metro(s) = {centimetros} centímetros.')
print(f'{metros} metro(s) = {milimetros} milímetros.')
