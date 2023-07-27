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

def loopInfinito():
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit' or event == 'Sair':
            break
        
        # consumindo arquivos
        if event == "-ARQUIVO-":
            
            pasta = values['-ARQUIVO-']

            try:
                fileList = os.listdir(pasta)

                filesNames = []
                

                for i in fileList:
                    if i.endswith((".py", ".xml", ".txt")):
                        filesNames.append(i)
                
                window['-LISTA-'].update(filesNames)

            except:
            
                pass
        
        # selecionando arquivo
        elif event == '-LISTA-':
            fileName = os.path.join(values['-ARQUIVO-'], values['-LISTA-'][0])

        # consumindo xml
        if event == "Buscar":
            if fileName.lower().endswith(".txt"):
                try:
                    with open(fileName, 'r') as arquivoInfo:
                        conteudo = arquivoInfo.read()

                    window['-OUTPUT-'].update(conteudo)
                except Exception as e:
                    window['-OUTPUT-'].update(f"Erro: {str(e)}")
            
            elif fileName.lower().endswith(".py"):
                try:
                    with open(fileName, 'r') as arquivoInfo:
                        conteudo = arquivoInfo.read()

                    window['-OUTPUT-'].update(conteudo)
                except Exception as e:
                        window['-OUTPUT-'].update(f"Erro: {str(e)}")

            else:
                window['-OUTPUT-'].update("Arquivo não suportado!")

        # sobre
        def sobreOSoftware():
            if event == "Sobre":
                show = '''
                ********************************************
                    Programador: Thiago Santos (V1.0)
                ********************************************
                '''
                sg.Popup(show)

        sobreOSoftware()
                

    window.close()

loopInfinito()
