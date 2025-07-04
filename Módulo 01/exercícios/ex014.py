# Leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
salario = float(input('Salário do funcionário: R$'))
aumento = (salario * 15) / 100
salario = salario + aumento
print(f'Ele receberá 15% de aumento e receberá R${aumento:.2f} a mais.')
print(f'Portanto, seu novo salário é de R${salario:.2f}')