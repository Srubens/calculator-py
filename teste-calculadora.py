import PySimpleGUI as sg 

sg.theme('DarkAmber')

layout = [
    [ sg.InputText(key='input') ],
    [sg.Button('AC', size=(4,2)), sg.Button('(', size=(4,2)), sg.Button(')', size=(4,2)), sg.Button('-', size=(4,2))],
    [sg.Button('7', size=(4,2)), sg.Button('8', size=(4,2)), sg.Button('9', size=(4,2)), sg.Button('+', size=(4,2))],
    [sg.Button('4', size=(4,2)), sg.Button('5', size=(4,2)), sg.Button('6', size=(4,2)), sg.Button('.', size=(4,2))],
    [sg.Button('1', size=(4,2)), sg.Button('2', size=(4,2)), sg.Button('3', size=(4,2)), sg.Button('*', size=(4,2))],
    [sg.Button('0', size=(10, 2)), sg.Button('=', size=(4, 2)), sg.Button('/', size=(4, 2))]
]

window = sg.Window('calculadora', layout, size=(220,300))

def operation():
    equation = text_entry
    result = eval(equation)
    window['input'].update(result)

text_entry = ''

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'AC':
        text_entry = ''
        window['input'].update(text_entry)
    elif event in '0123456789.+-*()/':
        text_entry = values['input']
        text_entry += event
        window['input'].update(text_entry)
    elif event in '=':
        operation()
    print(event)




window.close()
