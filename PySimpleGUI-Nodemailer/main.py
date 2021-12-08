import PySimpleGUI as sg
from urllib import request
import os
from processamento.verify import verify
import threading

layout = [
    [sg.Text('Email:', size=(10,0)), sg.Input(size=(30,0), key='remetente')],
    [sg.Text('Senha:', size=(10,0)), sg.Input(size=(30,0), password_char='*', key='senha')],
    [sg.Text('', key='msg')],
    [sg.Button('Logar')]
]

window = sg.Window('Login').layout(layout)

print('[!] - Programa iniciado.')

while True:
    event, value = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Logar':
        print('[!] - Iniciando a validação.')
        arquivo = open('.\\dados\\credenciais.json', 'w')

        json = f'''{{
    "email": "{value['remetente']}",
    "senha": "{value['senha']}"
}}'''
        arquivo.writelines(json)
        arquivo.close()

        def ligar():
            os.system('node .\\processamento\\validar.js')

        thread = threading.Thread(target=ligar).start()
        login = False

        try:
            if verify():
                print('[+] - A verificação foi concluida com exito.')
                window.close()
                exec(open('conteudo.py').read())
            else:
                print('[-] - A verificação foi mal sucedida.')
                window['msg'].update('Email ou senha invalido.')
        except:
            print('[-] - Erro.')
            sg.popup_error('Ocorreu um erro inesperado.')
            # que na verdade é bem esperadokk

print('[!] Programa fechado.')
os.system('del saida.txt')
window.close()
