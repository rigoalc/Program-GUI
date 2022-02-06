"""Encryption GUI

See: https://en.wikipedia.org/wiki/Caesar_cipher
"""
import string

import PySimpleGUI as sg

LETTERS = string.ascii_lowercase + string.ascii_uppercase
START = LETTERS
SHIFT_COUNT = 3
# Create new list with end of list shifted to the front
# Example shift of 3: 'ABCDEFG' -> 'EFGABCD'
END = LETTERS[-SHIFT_COUNT:] + LETTERS[:-SHIFT_COUNT]

ABOUT = """\
This program allows encrypting and decrypting text using the Caesar Cipher.\n
See https://en.wikipedia.org/wiki/Caesar_cipher for more info.
"""


def encrypt(plaintext):
    """Encrypt given plaintext"""
    convert = dict(zip(START, END))
    ciphertext = ''
    for letter in plaintext:
        ciphertext += convert.get(letter, letter)
    return ciphertext

def decrypt(ciphertext):
    """Decrypt given ciphertext"""
    convert = dict(zip(END, START))
    plaintext = ''
    for letter in ciphertext:
        plaintext += convert.get(letter, letter)
    return plaintext


class EncryptionGUI:
    """Encryption GUI"""
    def __init__(self):
        menu_def = [
            ['&File', ['&Quit']],
            ['&Help', ['&About...']],
        ]
        pad = (5, 1) # Tweak padding to make things look nicer
        layout = [
            # Add a menu at the top
            [sg.Menu(menu_def)],
            [sg.Input(size=(30,1), key='txt-plain', pad=pad), sg.Button('Encrypt', pad=pad)],
            [sg.Input(size=(30,1), key='txt-cipher', pad=pad), sg.Button('Decrypt', pad=pad)],
            # Add a status bar at the bottom
            [sg.StatusBar('This is the statusbar', key='status')]
        ]

        # Tweak padding and margins to make things look nicer
        self.window = sg.Window(
            'Encryption GUI', layout, element_padding=(0, 0), margins=(0, 0),
            resizable=True, finalize=True)
        self.window['txt-plain'].expand(True)
        self.window['txt-cipher'].expand(True)

    def run(self):
        """Start the program"""
        # Start the Event Loop
        self._run_loop()
        # After that is done, close the window
        self.window.close()

    def _run_loop(self):
        """Run the Event Loop"""
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED or event == 'Quit':
                break
            elif event == 'Encrypt':
                self._on_encrypt(event, values)
            elif event == 'Decrypt':
                self._on_decrypt(event, values)
            elif event == 'About...':
                self._on_about(event, values)

    def _on_encrypt(self, event, values):
        """Handle when Encrypt button is clicked"""
        plaintext = values['txt-plain']
        self.window['txt-cipher'].update(encrypt(plaintext))
        self.window['status'].update("Encrypted")

    def _on_decrypt(self, event, values):
        """Handle when Decrypt button is clicked"""
        ciphertext = values['txt-cipher']
        self.window['txt-plain'].update(decrypt(ciphertext))
        self.window['status'].update("Decrypted")

    def _on_about(self, event, values):
        """Show About Dialog"""
        sg.popup("About Dialog", ABOUT)

# Instantiate our class and run it
gui = EncryptionGUI()
gui.run()