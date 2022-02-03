#
import PySimpleGUI as sg
from datetime import date


layout = [
    [sg.Text("Enter your birthay to calculate your age:")],
    [sg.Input(size=(10,1), key='birthmonth'), sg.Input(size=(10,1), key='birthday'), sg.Input(size=(10,1), key='birthyear')],
    [sg.Text('Result:'), sg.Text(key='result')],
    [sg.Button('Calc'), sg.Button('Quit')],
]

window = sg.Window('Leap Years', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    elif event == 'Calc':
        today = date.today
        one_or_zero = ((today.month, today.day) < (int(values['birthmonth']),int(values['birthday'])))
        year_difference = today.year - int(values['birthyear'])
        age = year_difference - one_or_zero
        result = age
        window['result'].update(result)


window.close()
