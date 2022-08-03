from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkcode import *
from tkinter import messagebox
import subprocess
import tkinter as tk

#This ide is just a simple one that focus on the aboslute basics of Tkinter
#Next features : Fix Stop button, Output set to = readonly, Tabs supports
#Thank you for trying my IDE

root = Tk()
root.title('LTK IDE BETA CODENAME CYBERWARRIOR')
file_path = ''

#Still BETA Until i figure out some other UI Problems ; )
notebook = ttk.Notebook()
notebook.pack(pady=10, fill=BOTH)
Widgets = [

    ["Create\nWindow",
     "import tkinter as tk\n\nroot=tk.Tk()\nroot.geometry('300x300')\n\nroot.mainloop()"],
    ["Button", "\nb1 = tk.Button(root, text='Hello World')\nb1.pack()"],
    ["Entry", "\ne1 = tk.Entry(root)\ne1.pack()"],
    ["Checkbutton", "\ncb = tk.Checkbutton(root, text='Hello World')\ncb.pack()"],
    ["Radiobutton", "\nrb = tk.Radiobutton(root, text='Hello World')\nrb.pack()"],
    ["Label", "\nl1 = tk.Label(root, text='Hello World')\nl1.pack()"],
    ["Listbox", "\nl_b = tk.Listbox(root)\nl_b.pack()"],
    ["Text", "\nt = tk.Text(root)\nt.pack()"],
    ["Frame", "\nf1 = tk.Frame(root)\nf1.pack()"],
    ["Menu", "\nm1 = tk.Menu(root)\nm1.add_command(label='Hello World')\nroot.config(menu=m1)"],
    ["Scale", "\ns1 = tk.Scale(root, from_=0, to=100)\ns1.pack()"],
    ["Scrollbar", "\nsb = tk.Scrollbar(root)\nsb.pack()"]

]

def set_file_path(path):
    global file_path
    file_path = path

def stop():

    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    process.kill()


def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)


def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)

def run():
    if file_path == '':
        messagebox.showinfo(title='Unsaved Change Detected', message='Please Save Your File Then Continue !' )
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0',  error)

def insert_code(Code):
    editor.insert(tk.INSERT, Code)

def msg():
    messagebox.showinfo(message='LTK IDE, Light Tkinter IDE, Made by GG_Youssef, ! CyberWarrior, 2020-2022', title='About LTK')

menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)

add_menu = Menu(menu_bar)
add_menu.add_command(label='Add Window', command=lambda: insert_code(Widgets[0][1]))
add_menu.add_command(label='Add Button', command=lambda: insert_code(Widgets[1][1]))
add_menu.add_command(label='Add Text Box', command=lambda: insert_code(Widgets[7][1]))
add_menu.add_command(label='Add Label', command=lambda: insert_code(Widgets[5][1]))
add_menu.add_command(label='Add Frame', command=lambda: insert_code(Widgets[8][1]))
add_menu.add_command(label='Add Menu', command=lambda: insert_code(Widgets[9][1]))
add_menu.add_command(label='Add Entry', command=lambda: insert_code(Widgets[2][1]))
add_menu.add_command(label='Add Scale', command=lambda: insert_code(Widgets[10][1]))
add_menu.add_command(label='Add Scroll Bar', command=lambda: insert_code(Widgets[11][1]))
add_menu.add_command(label='Add Radio Button', command=lambda: insert_code(Widgets[4][1]))
add_menu.add_command(label='Add List Box', command=lambda: insert_code(Widgets[6][1]))
add_menu.add_command(label='Add Check Box', command=lambda: insert_code(Widgets[3][1]))
menu_bar.add_cascade(label='Tkinter GUI', menu=add_menu)

about_menu = Menu(menu_bar)
menu_bar.add_cascade(label='About LTK IDE', command=msg)

frame = tk.Frame(notebook, bg='#212121')
frame.pack_propagate(False)
frame.config(height=50)
frame.pack(fill=BOTH)

stop_btn = tk.Button(frame, text='Stop', bg='#272727', fg='red',
                    font=('Consolas', 15),
                    command=run)
stop_btn.config()
stop_btn.pack(side=RIGHT, padx=10,pady=10, fill=Y)

run_btn = tk.Button(frame, text='Run', bg='#272727', fg='lime',
                    font=('Consolas', 15),
                    command=run)
run_btn.config()
run_btn.pack(side=RIGHT, padx=10,pady=10, fill=Y)

root.config(menu=menu_bar)

editor = CodeEditor(
    notebook,
    width=40,
    height=25,
    language="Python",
    highlighter="dracula",
    autofocus=True,
    font="Consolas",
    blockcursor=True,
    insertofftime=0,
    padx=10,
    pady=10,
)
editor.pack(fill=BOTH, expand=True)


code_output = Text(notebook, width=10)
code_output.pack(fill=BOTH)
root.mainloop()
