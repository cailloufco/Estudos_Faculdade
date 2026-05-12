livros_cadastrados = dict()

while True:
    op = int(input('''
1- Cadastrar Livro
2- Listar Livros
3- Atualizar Livro
4- Remover Livro
0- Sair
Opção: '''))
    
    if op == 1:
        isbm = int(input('Digite o ISBM: '))
        if isbm in livros_cadastrados:
            print('Livro já cadastrado')
            continue
        
        titulo_livro = input('Qual o titulo do livro?: ')
        autor = input('Qual o autor do livro?: ')
        ano = int(input('Em qual ano o livro foi escrito?: '))
        livros_cadastrados[isbm] = {'titulo': titulo_livro,
                                     'autor': autor,
                                     'ano': ano}

    elif op == 2:
        for isbn in livros_cadastrados:
            print(f"{livros_cadastrados[isbn] ['titulo']}")

    elif op == 3:
        busca_atualizar = int(input('Qual livro deseja atualizar? (BUSCA POR ISBM): '))
        
        if busca_atualizar in livros_cadastrados:
            titulo_livro = input('Qual o titulo do livro?: ')
            autor = input('Qual o autor do livro?: ')
            ano = int(input('Em qual ano o livro foi escrito?: '))
            livros_cadastrados[busca_atualizar] = {'titulo': titulo_livro, 'autor': autor, 'ano': ano}

    elif op == 4:
        busca_remover = int(input('Qual livro deseja remover? (REMOÇÃO POR ISBM): '))
        if busca_remover in livros_cadastrados:
            livros_cadastrados.pop(busca_remover)
            print('Livro removido.')