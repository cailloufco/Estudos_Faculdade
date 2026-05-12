jogadores = dict()

while True:
    op = int(input('''1 - Cadastrar jogador
2 - Vizualizar jogadores cadastrados
3 - Atualizar status de um jogador
4 - Remover jogador
0 - Sair'''))
    if op == 1:
        nome = input('Digite seu nome: ')
        if nome in jogadores:
            print('jogador ja registrado')
            continue
        idade = int(input('Digite sua idade: '))
        esporte = input('Digite qual esporte você joga: ')
        jogadores[nome] = {'idade': idade,
                           'esporte': esporte}
    elif op == 2:
        for jogador in jogadores:
            print(f"NOME - {jogador}\nIDADE - {jogadores[jogador]['idade']}\nESPORTE - {jogadores[jogador]['esporte']}\n\n")
    elif op == 3:
        escolha = input('Qual jogador deseja atualizar os dados?: ')
        if escolha in jogadores:
            idade = int(input('Digite sua idade: '))
            esporte = input('Digite qual esporte você joga: ')
            jogadores[escolha] = {'idade': idade,
                            'esporte': esporte}
    elif op == 4:
        escolha = input('Qual jogador deseja remover os dados?: ')
        if escolha in jogadores:
            jogadores.pop(escolha)