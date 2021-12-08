import PySimpleGUI as sg
import os

from layout import manuseio, estoque
from funcoes import cadastrar, deletar, aumentar, baixa

layout = [
    [sg.TabGroup([[sg.Tab('Manuseio', manuseio), sg.Tab('Estoque', estoque)]])],
]

window = sg.Window('Almoxarifado', layout, size=(460, 500))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Cadastrar':
        try:
            nome = values['nome'].capitalize().strip()
            preco = values['preco'].replace(',', '.')
            qnt = int(values['qnt_cadastro'])
            preco = float(preco)
        except:
            window['cadastro_text'].update('Por favor, adicione valores validos.')
        else:
            window['cadastro_text'].update('')
            if preco >= 0 and qnt >= 0:
                cadastrar(nome, str(f'{preco:.2f}'), qnt)
            else:
                window['cadastro_text'].update('Por favor, adicione valores validos.')

    if event == 'Remover':
        nome = values['nome_remover']
        window['remover_text'].update('')
        deletar(nome)
    
    if event == 'Alterar':
        try:
            nome = values['nome_alteracao']
            qnt = int(values['qnt_alteracao'])
        except:
            window['alteracao_text'].update('Por favor, adicione valores validos.')
        else:
            window['alteracao_text'].update('')
            if values['aumentar']:
                aumentar(nome, qnt)
            
            else:
                baixa(nome, qnt)     

window.close()
