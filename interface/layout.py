import PySimpleGUI as sg
import os, sys

import os.path
import io
import base64

sg.theme('DarkGrey12')

menu = [
    ["Aquivo", ["Sobre", "Sair"]]
]


butoes = [
    [sg.Button('Buscar'), sg.Text('XML'), sg.In(size=(20,1), enable_events=True, key='-ARQUIVO-'), sg.FolderBrowse("Procurar Arquivo")],
    [sg.Listbox(values=[], enable_events=True, size=(55,20),key='-LISTA-')],
]

resultado = [
    [sg.Output(size=(50, 30), key='-OUTPUT-')]
]


layout = [
    [
    sg.Menu(menu),
    sg.Column(butoes),
    sg.VSeperator(),
    sg.Column(resultado)
    ]   
]

window = sg.Window('NFS-e', layout, resizable=True, finalize=True)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit' or event == 'Sair':
        break

    if event == "Procurar Arquivo":
        pasta = values['-ARQUIVO-']

        try:
            fileList = os.listdir(pasta)
        except:
           fileList = []

           fnames = [f for f in fileList if os.path.isfile(
               os.path.join(pasta, f)) and f.lower().endswith((".py", ".xml", ".txt"))]
           
           window['-LISTA-'].update(fnames)

    if event == "Buscar":
        print("teste Buscar")
        

window.close()

