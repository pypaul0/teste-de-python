# programa que abre site
from urllib import request
import webbrowser
from função_de_cor import cor

prefixos = 'https://www.','https://', 'http://www.', 'http://',
funcionou = False
verif = False

while True:
    try:
        url = str(input(cor('Digite o site que você deseja abrir: ', 'amarelo')))
    except KeyboardInterrupt:
        print(cor('\nO usuario encerrou o programa.', 'vermelho', neg=True))
        break
    url_copy = url
    # correção de url
    for p in prefixos:
        if p in url:
            verif = True
            break
    for p in prefixos:
        if p not in url and not verif:
            url = p + url_copy
        try:
            request.urlopen(url)
        except:
            continue
        else:
            webbrowser.open(url)
            funcionou = True
            break
    # mostra se funcionou ou não
    if funcionou:
        print(cor(f'O site {url} foi aberto', 'verde', neg=True))
        break

    if not funcionou:
        print(cor(f'O site {url_copy} não está acessivel :(', 'vermelho', neg=True))
