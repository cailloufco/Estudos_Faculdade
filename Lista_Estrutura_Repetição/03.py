'''
3. Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';
'''


while True:
    nome = input('Digite seu nome: ')
    if len(nome) > 3:
        break
    else:
        print('nome inválido!')
while True:
    idade = int(input('Digite sua idade: '))
    if idade < 0 or idade > 150:
        print('idade inválida')
    else:
        break
while True:
    salario = float(input('Digite seu salário: '))
    if salario < 0:
        print('salário inválido!')
    else:
        break
while True:
    sexo = input("Diga seu sexo 'f' ou 'm': ").lower()
    if len(sexo) > 1:
        print("Digite apenas 'f' ou 'm'!")
        continue
    if sexo != 'f' and sexo != 'm':
        print('Escolha inválida')
    else:
        break
while True:
    #e. Estado Civil: 's', 'c', 'v', 'd';
    estado_civil = input('Diga seu estado civil (S , C , V , D):').lower()
    if estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd':
        break
    else:
        print('Escolha inválida')
print(f'Nome: {nome}\nIdade: {idade}\nSalário: {salario}\nSexo: {sexo.upper()}\nEstado Civil: {estado_civil.upper()}')