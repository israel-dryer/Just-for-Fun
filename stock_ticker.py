# scrolling message bar
import time
import PySimpleGUI as sg 

msg = 'S&P 500: 2,906.27 | Dow 30 26,118.02 | Nasdaq 7,874.16 | '
layout = [[sg.Text(msg , font=('Franklin Gothic Book', 25), key='_DISPLAY_')]]
window = sg.Window('Message Scroller', layout=layout)

timeout = 0.3

while True:
    size = len(msg)+1
    x = 0
    while True:
        event, values = window.read(timeout=timeout)
        front = msg[:x]
        back = msg[x:]
        window['_DISPLAY_'].update(value=back + front)
        time.sleep(timeout)
        if x == size:
            x = 0
        else:
            x += 1