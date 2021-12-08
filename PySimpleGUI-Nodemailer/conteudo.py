import PySimpleGUI as sg
import os


layout = [
    [sg.Text('Destinatario:', size=(10,0)), sg.Input(size=(30,0), key='destinatario')],
    [sg.Text('Titulo:', size=(10,0)), sg.Input(size=(30,0), key='titulo')],
    [sg.Text('Conteudo:', size=(10,7)), sg.Multiline(size=(30,7), key='conteudo')],
    [sg.Text('', key='msg')],
    [sg.Button('Enviar')]
]

window = sg.Window('Email').layout(layout)
print('[!] - Iniciando tela de Email.')
while True:
    event, value = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Enviar':
        arquivo = open('.\\dados\\corpo.json', 'w', encoding='UTF-8')

        if value['conteudo'].count('\n') > 1:
            window['msg'].update('Por favor, remova as quebras de linha.')
            
        else:
            json = f'''{{
        "destinatario": "{value['destinatario']}",
        "titulo": "{value['titulo']}",
        "conteudo": "{value['conteudo'][:-1]}"
}}'''
            arquivo.writelines(json)
            arquivo.close()

            os.system('node .\\processamento\\email.js')

window.close()