from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import filedialog
import time

window = Tk()


def open_file():
    name = filedialog.askopenfilename(initialdir="/",
                                      filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
                                      title="Choose a file."
                                      )
    print(name)
    try:
        with open(name, 'r') as UseFile:
            print(UseFile.read())
    except:
        print("No file exists")


def open_directory():
    directory = filedialog.askdirectory()
    print(directory)


# def start_process():
#     print(outputFileName)
#     progress['value'] = 20
#     window.update_idletasks()
#     time.sleep(1)
#     progress['value'] = 50
#     window.update_idletasks()
#     time.sleep(1)
#     progress['value'] = 80
#     window.update_idletasks()
#     time.sleep(1)
#     progress['value'] = 100


def start_process():
    import threading

    def start_thread():
        progress.start()
        time.sleep(5)
        progress.stop()

        startButton['state'] = 'normal'
        errorMsg['text'] = 'Successfully Done'
        errorMsg['foreground'] = 'green'

    startButton['state'] = 'disabled'
    errorMsg['text'] = 'Processing...'
    errorMsg['foreground'] = 'blue'
    threading.Thread(target=start_thread).start()


window.minsize(200, 200)

window.title("Small Tkinter GUI")
title = ttk.Label(window, text="Tkinter", foreground="blue", font=("Helvetica", 16))
title.pack(padx=20, pady=20)

inputFilePicker = Button(window, text="Select Input File", command=open_file)
inputFilePicker.pack(padx=5, pady=5)

outputDirectoryPicker = Button(window, text="Select Output Directory", command=open_directory)
outputDirectoryPicker.pack(padx=5, pady=5)

outputFileName = Entry(window)
outputFileName.pack(padx=5, pady=5)

errorMsg = Label(window, text="", foreground="red")
errorMsg.pack(padx=5, pady=5)

progress = Progressbar(window, orient=HORIZONTAL, length=100, mode='indeterminate')
progress.pack(padx=5, pady=5)

startButton = Button(window, text="Start", command=start_process)
startButton.pack()

menu = Menu(window)
window.config(menu=menu)

file = Menu(menu)

file.add_command(label='Open', command=open_file)
file.add_command(label='Exit', command=lambda: exit())

menu.add_cascade(label='File', menu=file)

window.mainloop()
