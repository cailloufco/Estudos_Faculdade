'''
11. Altere o programa anterior para mostrar no final a soma dos números
'''
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
soma = 0
for i in range(num1, num2+1):
    print(i , end=' ')
    soma += i
print('\n',soma)