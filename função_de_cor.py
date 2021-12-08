def cor(msg, cor, neg=False):
    '''
    msg = a mensagem que você quer colorir.
    cor = a cor que você deseja.
    neg = se quer em negrito ou não. (opcional)

    cores disponiveis:         
        preto
        vermelho
        verde
        amarelo
        azul
        roxo
        ciano
        cinza
    '''
    cores = {
        'preto': '\033[30m',
        'vermelho': '\033[31m',
        'verde': '\033[32m',
        'amarelo': '\033[33m',
        'azul': '\033[34m',
        'roxo': '\033[35m',
        'ciano': '\033[36m',
        'cinza': '\033[37m',
    }
    if neg:
        return f'\033[1m{cores[cor]}{msg}\033[m'
    return f'{cores[cor]}{msg}\033[m'
