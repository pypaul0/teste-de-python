def escreve_no_texto_um_monte_de_vez(text, qnt):
    por = control = 0 
    try:
        arquivo = open('text.txt', 'r')
    except:
        arquivo = open('text.txt', 'w', encoding='UTF-8')
        arquivo = open('text.txt', 'r')

    conteudo = arquivo.readlines()

    for i in range(0, qnt):
        conteudo.append(text)
        por = int(i*100/qnt)
        if por != control:
            control = por
            print(f'{por}%')
    arquivo = open('text.txt', 'w', encoding='UTF-8')
    arquivo.writelines(conteudo)
    arquivo.close()
    print('100%')
