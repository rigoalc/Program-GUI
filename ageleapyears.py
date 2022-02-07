
# Rodrigo Alcover
# Program Search and Sort due 1/29/2022
# CIS 226-23199 Advanced Python Programming
# 8hrs

'''Design: How will you solve the problem?
I will solve this problem installing libraries like PySimpleGUI that willl permit have run a Graphical User Interface.
And creating a logical function to calculate values and return a result to the user by the GUI interface.

Develop:
First created a basic version of the prgram. Then add to that features included with the library, 
and divided the code in functions inside one class.

Test:
The idea is to test assering a simple calculation using a virtual enviroment runing pytest from the trminal.

How to use the program:
Open the program, introduce a day of birth, click button "Calc" to get the age. This program is calculating the leap years for that 
birthyear, month, and day.

 '''

import PySimpleGUI as sg
from datetime import date

ABOUT = """This program calculates the age solving the problem of the Leap Years for the birthday count.
Calculating the age by counting the days from the birthday is incorrect; the correct way to calculate 
is substracting the birth year from the current year and then subtract one more year 
if the current month/day comes before the user's birth month/day.
"""
class Age:
    def __init__(self):
        menu_def = [#menu
            ['&File', ['&Quit']],
            ['&Help', ['&About...']],
        ]
        pad = (5, 1)
        layout = [#Window
            [sg.Menu(menu_def)],
            [sg.Text("Enter your birthay mm/dd/yyyy to calculate your age:")],
            [sg.Input(size=(10,1), key='birthmonth', pad=pad), sg.Input(size=(10,1), key='birthday', pad=pad), sg.Input(size=(10,1), key='birthyear', pad=pad)],#This input format format to .date
            [sg.Text('Result:'), sg.Text(key='result')],
            [sg.Button('Calc'), sg.Button('Quit')],
            [sg.StatusBar('This is the statusbar', key='status')]
        ]
        self.window = sg.Window('Calculate Your Age', layout, element_padding=(0, 0), margins=(0, 0),
            resizable=True, finalize=True)
    def run(self):
        # Start the Event Loop
        self.age_leap_years()
        # After that is done, close the window
        self.window.close()
    def age_leap_years(self):
        while True:#Loop
            event, values = self.window.read()#wait
            if event == sg.WINDOW_CLOSED or event == 'Quit':#if detect action from the user to exit
                break#actual stop/exit
            elif event == 'About...':#User push 'calc' button
                sg.popup("About Dialog", ABOUT)#Pop the ABOUT message
            elif event == 'Calc':#User push 'calc' button
                today = date.today()
                one_or_zero = ((today.month, today.day) < (int(values['birthmonth']),int(values['birthday'])))#compare and have a one or cero value if the user birthay has passed the current year
                year_difference = today.year - int(values['birthyear'])#calculate the years old 
                age = year_difference - one_or_zero#Discount or not one year 
                result = age#actual age
                self.window['result'].update(result)
                self.window['status'].update("Done!")

if __name__ == '__main__': 

    gui = Age()
    gui.run()

