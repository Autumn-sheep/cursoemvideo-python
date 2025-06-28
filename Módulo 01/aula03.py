# Operadores Aritméticos e Ordem de precedência

# ()
# **
# *, /, // e %
# + -

# Para realizar potenciação sem operador, usa-se a função pow()
print(f'4² -> {pow(4, 2)}')

# Para realizar operações de raiz quadrada:
print(f'Raiz quadrada de 81 -> {81 ** (1/2)}')
print(f'Raiz cúbica de 81 -> {81 ** (1/3)}')

# Alinhamentos de string
nome = "Deadmau5"
print('-=-' * 20)
print(f'ALINHANDO STRINGS COM 20 CARACTERES!')
print(f'À esquerda: {nome:<20}!')
print(f'À direita: {nome:>20}!')
print(f'Centralizado: {nome:^20}!')
print(f'Preencher espaços com o nome centralizado: {nome:=^20}!')
