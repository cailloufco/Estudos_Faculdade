'''
8. Faça um programa que leia 5 números e informe a soma e a média dos números.
'''
media = 0
for i in range(5):
    i = float(input(f'{i+1}-Digite 5 numeros: '))
    media += i
print(media/5)