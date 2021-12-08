import PySimpleGUI as sg

cont = 0
produtos = None

with open('produtos.txt') as file:
    produtos = file.readlines()[:]
    cont = len(file.readlines())

cadastro = [
    [sg.Text('Nome:'), sg.Input(key='nome')],
    [sg.Text('Preço R$:'), sg.Input(key='preco')],
    [sg.Text('Quantidade:'), sg.Input(key='qnt_cadastro')],
    [sg.Text('', key='cadastro_text')],
    [sg.Button('Cadastrar')]
]

remover = [
    [sg.Text('Nome:'), sg.Input(key='nome_remover')],
    [sg.Text('', key='remover_text')],
    [sg.Button('Remover')]
]

alteracao = [
    [sg.Text('Nome:'), sg.Input(key='nome_alteracao')],
    [sg.Text('Quantidade:'), sg.Input(key='qnt_alteracao')],
    [sg.Radio('Aumentar', 'ALTERACAO', key='aumentar', default=True), sg.Radio('Diminuir', 'ALTERACAO', key='diminuir')],
    [sg.Text('', key='alteracao_text')],
    [sg.Button('Alterar')]
]

manuseio = [
    [sg.Frame('Cadastro de produto', cadastro)],
    [sg.Frame('Remoção de produto', remover)],
    [sg.Frame('Alteração de produto', alteracao)]
]

# -----------------------------------------------

titulo = ['NOME', 'ESTOQUE', 'PREÇO']

cabecalho = [
    [sg.Text(f'{t: ^26}') for t in titulo]
]

corpo = [
    [sg.Input(p.split(';')[c].replace('.', ','), size=(20,1), pad=(0,0), disabled=True) for c in range(3)] for p in produtos
]

estoque = cabecalho + corpo

