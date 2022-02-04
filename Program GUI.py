#
import PySimpleGUI as sg
from datetime import date


layout = [
    [sg.Text("Enter your birthay to calculate your age:")],
    [sg.Input(size=(10,1), key='birthmonth'), sg.Input(size=(10,1), key='birthday'), sg.Input(size=(10,1), key='birthyear')],#This input format format to .date
    [sg.Text('Result:'), sg.Text(key='result')],
    [sg.Button('Calc'), sg.Button('Quit')],
]

window = sg.Window('Calculate your years', layout)

while True:#Loop
    event, values = window.read()#wait
    if event == sg.WINDOW_CLOSED or event == 'Quit':#if detect action from the user to exit
        break#actual stop/exit
    elif event == 'Calc':#User push 'calc' button
        today = date.today()#Today date
        one_or_zero = ((today.month, today.day) < (int(values['birthmonth']),int(values['birthday'])))#compare and have a one or cero value if the user birthay has passed the current year
        year_difference = today.year - int(values['birthyear'])#calculate the years old 
        age = year_difference - one_or_zero#Discount or not one year 
        result = age#actual age
        window['result'].update(result)


window.close()
