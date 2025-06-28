# Tipos Primitivos
# int() -> inteiro, ex: 15, -1, 0
# float() -> ponto flutuante, ex: 0.75, 0.99
# bool -> True, False
# str() -> sequência de caracteres
num = 10
money = 70.70
true_or_false = True
msg = "Asuka"

print(f'Number: {num} - - {type(num)}')
print(f'Money: R${money:.2f} - - {type(money)}')
print(f'True or false? {true_or_false} - - {type(true_or_false)}')
print(f'Message: {msg} - - {type(msg)}')

print(f'-=-' * 20)

# MÉTODOS COM STRING
print(f'Alphabetic? {msg.isalpha()}')
print(f'Alphanumeric? {msg.isalnum()}')
print(f'Is it in upper case? {msg.isupper()}')