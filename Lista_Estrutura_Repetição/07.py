'''
7. Faça um programa que leia 5 números e informe o maior número.
'''
maior_numero = None
for i in range(5):
    i = int(input(f'{i+1}- Digite cinco numeros: '))
    if maior_numero == None:
        maior_numero = i
    if i > maior_numero:
        maior_numero = i
print(maior_numero)