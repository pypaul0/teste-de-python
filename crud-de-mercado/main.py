from funcoes import cadastrar, mostrar, deletar, baixa, aumentar

while True:
    print('-'*40)
    print(f"{'MENU PRINCIPAL':^40}")
    print('-'*40)
    print('''[1] - CADASTRAR PRODUTO
[2] - CONSULTAR PRODUTO
[3] - APAGAR PRODUTO
[4] - DAR BAIXA NO ESTOQUE
[5] - AUMENTAR O ESTOQUE
[6] - SAIR DO PROGRAMA''')
    try:
        escolha = str(input('Digite sua escolha: '))

        while not escolha.isnumeric() or escolha not in '123456':
            escolha = str(input('Por favor escolha uma opção valida: '))

    except KeyboardInterrupt:
        break

    escolha = int(escolha)

    if escolha == 1:
        print('-'*40)
        print(f"{'CADASTRO DE PRODUTO':^40}")
        print('-'*40)
        try:
            nome = str(input('Nome: '))

        except KeyboardInterrupt:
            break

        preco = 0
        estoque = -1

        while type(preco) != float:
            try:
                preco = str(input('Preço: ')).replace(',', '.')
                preco = float(preco)
                
            except KeyboardInterrupt:
                quit()

            except:
                continue

        while estoque < 0:
            try:
                estoque = int(input('Estoque: '))

            except KeyboardInterrupt:
                quit()

            except:
                continue

        cadastrar(nome, preco, estoque)

    if escolha == 2:
        print('-'*40)
        print(f"{'PRODUTOS':^40}")
        print('-'*40)
        print(f'{"ID": <8}{"Nome": <12}{"Estoque": <10}{"Preço"}')

        mostrar()

    if escolha == 3:
        print('-'*40)
        print(f"{'DELETAR PRODUTO':^40}")
        print('-'*40)

        cont = 0
        with open('produtos.txt') as file:
            cont = len(file.readlines())
            
        print(f'{"ID": <8}{"Nome": <12}{"Estoque": <10}{"Preço"}')
        mostrar()
        remove = 0

        while remove < 1 or remove > cont:
            try:
                remove = int(input('Digite o ID do produto: '))

            except KeyboardInterrupt:
                quit()

            except:
                continue

        deletar(remove)

    if escolha == 4:
        print('-'*40)
        print(f"{'BAIXA NO ESTOQUE':^40}")
        print('-'*40)

        item = -1
        qnt = -1
        cont = 0
        with open('produtos.txt') as file:
            cont = len(file.readlines())

        mostrar()

        while item <= 0 or item > cont:
            try:
                item = int(input('Digite o ID do produto: '))

            except KeyboardInterrupt:
                quit()

            except:
                continue

        with open('produtos.txt') as file:
            file = file.readlines()[item-1]
            file = file.split(';')
            quantidade_estoque = int(file[1])

        while qnt < 0 or qnt > quantidade_estoque:
            try:
                qnt = int(input('Digite a quantidade: '))

            except KeyboardInterrupt:
                quit()

            except:
                continue

        baixa(item, qnt)

    if escolha == 5:
        print('-'*40)
        print(f"{'AUMENTO NO ESTOQUE':^40}")
        print('-'*40)

        item = -1
        qnt = -1
        cont = 0
        with open('produtos.txt') as file:
            cont = len(file.readlines())

        mostrar()

        while item <= 0 or item > cont:
            try:
                item = int(input('Digite o ID do produto: '))

            except KeyboardInterrupt:
                quit()

            except:
                continue

        with open('produtos.txt') as file:
            file = file.readlines()[item-1]
            file = file.split(';')
            quantidade_estoque = int(file[1])

        while qnt <= 0:
            try:
                qnt = int(input('Digite a quantidade: '))

            except KeyboardInterrupt:
                quit()

            except:
                continue

        aumentar(item, qnt)

    if escolha == 6:
        break
