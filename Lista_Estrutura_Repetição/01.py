'''
1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''

while True:
    nota = float(input('Digite uma nota entre zero e dez'))
    if nota > 10 or nota < 0:
        print('Nota inválida! Tente novamente...')
    else:
        print('Nota válida!!!')
        break
