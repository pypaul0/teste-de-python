def cadastrar(nome, preco, estoque):
    with open('produtos.txt', encoding='utf8') as file:
        copy = file.readlines()

    with open('produtos.txt', 'w', encoding='utf8') as file:
        file.writelines(copy)
        file.writelines(f'{nome};{estoque};{preco}\n')


def deletar(item):
    with open('produtos.txt', encoding='utf8') as file:
        novo = list()

        for linha in file:
            nome = linha.split(';')[0]
            if nome != item:
                novo.append(linha)

    with open('produtos.txt', 'w', encoding='utf8') as file:
        file.writelines(novo)


def baixa(item, qnt):
    with open('produtos.txt', encoding='utf8') as file:
        novo = list()

        for linha in file:
            nome = linha.split(';')[0]
            if nome == item:
                dado = linha.split(';')
                dado[1] = int(dado[1]) - qnt
                linha = f'{dado[0]};{dado[1]};{dado[2]}'

            novo.append(linha)

    with open('produtos.txt', 'w', encoding='utf8') as file:
        file.writelines(novo)


def aumentar(item, qnt):
    with open('produtos.txt', encoding='utf8') as file:
        novo = list()

        for linha in file:
            nome = linha.split(';')[0]
            if nome == item:
                dado = linha.split(';')
                dado[1] = int(dado[1]) + qnt
                linha = f'{dado[0]};{dado[1]};{dado[2]}'

            novo.append(linha)

    with open('produtos.txt', 'w', encoding='utf8') as file:
        file.writelines(novo)
