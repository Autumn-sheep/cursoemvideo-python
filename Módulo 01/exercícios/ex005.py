# Leia algo pelo teclado e mostre seu tipo primitivo e possíveis informações da mensagem
msg = str(input('Digite algo aqui: '))

print(f'''
Checando informações...
Contém apenas letras? {msg.isalpha()}
Contém apenas números? {msg.isnumeric()}
É alfanúmerico? {msg.isalnum()}
Está em maiúsculo? {msg.isupper()}
''')
