import PySimpleGUI as sg

from logic import csv_convert as cc

path: str = ""
overwrite: bool = False

sg.theme('Topanga')

layout = [
    [
        sg.Text(f"Path: {path}", key='-PATH-', size=(24, 4), auto_size_text=True),
        sg.FileBrowse("Select File", key='-FILES-', file_types=(('CSV ファイル', '*.csv'),)),
    ],
    [
        sg.Text("Name:", justification='right'),
        sg.InputText('', key="-NAME-", enable_events=True),
    ],
    [
        sg.Checkbox("Overwrite", default=overwrite, key='-OVERWRITE-'),
    ],
    [
        sg.Button("Wide2Long!!", key='-WIDE-2-LONG-', size=(12, 1)),
    ],
    [
        sg.Output(size=(40, 6))
    ]
]

window = sg.Window(title="CSV editor", layout=layout, size=(320, 240), resizable=False)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'exit': break
    path = values['-FILES-']
    if event == '-WIDE-2-LONG-': 
        cc.wide2long(path, values['-NAME-'], values['-OVERWRITE-'])
        print("Wide2Long done!!")
    print(values['-NAME-'], values['-OVERWRITE-'])

window.close()