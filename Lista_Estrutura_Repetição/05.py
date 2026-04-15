'''
5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a
entrada e permita repetir a operação.
'''
contador = 0
populacao_A = float(input('Digite a população de A: '))
taxa_A = (float(input('Diga quantos PORCENTO por ano a população de A aumenta: ')) / 100) + 1
populacao_B = float(input('Digite a população de B: '))
taxa_B = (float(input('Diga quantos PORCENTO por ano a população de B aumenta: ')) / 100) + 1
# A população do país A ultrapasse ou iguale a população do país B

if taxa_A <= taxa_B:
    print('As taxas ditas estão inválidas para a execução do codico!')
    exit()
if populacao_B < populacao_A:
    print('O exercicio anterior propoe que a População de A tenha que ultrapação ou igualar a População de B , logo B nao pode ser menor que A')
    exit()
while populacao_B > populacao_A:
    populacao_A *= taxa_A
    populacao_B *= taxa_B
    contador += 1
print(f'{contador} anos , {populacao_A//1} e {populacao_B//1}')