def cadastrar(nome, preco, estoque):
    with open('produtos.txt', 'a', encoding='utf8') as file:
        file.write(f'{nome};{estoque};{preco}\n')


def mostrar():
    with open('produtos.txt', encoding='utf8') as file:
        for pos, linha in enumerate(file):
            dado = linha.split(';')
            dado[2] = dado[2].replace('\n', '')
            preco = f'{float(dado[2]): <7.2f}'
            print(
                f'{f"[{pos+1}] - ": <8}{dado[0]: <12}{dado[1]: <10}R$: {str(preco).replace(".", ",")}')


def deletar(item):
    with open('produtos.txt', encoding='utf8') as file:
        novo = list()

        for pos, linha in enumerate(file):
            if pos != item-1:
                novo.append(linha)

    with open('produtos.txt', 'w', encoding='utf8') as file:
        file.writelines(novo)


def baixa(item, qnt):
    with open('produtos.txt', encoding='utf8') as file:
        novo = list()

        for pos, linha in enumerate(file):
            if pos == item-1:
                dado = linha.split(';')
                dado[1] = int(dado[1]) - qnt
                linha = f'{dado[0]};{dado[1]};{dado[2]}'

            novo.append(linha)

    with open('produtos.txt', 'w', encoding='utf8') as file:
        file.writelines(novo)


def aumentar(item, qnt):
    with open('produtos.txt', encoding='utf8') as file:
        novo = list()

        for pos, linha in enumerate(file):
            if pos == item-1:
                dado = linha.split(';')
                dado[1] = int(dado[1]) + qnt
                linha = f'{dado[0]};{dado[1]};{dado[2]}'

            novo.append(linha)

    with open('produtos.txt', 'w', encoding='utf8') as file:
        file.writelines(novo)
