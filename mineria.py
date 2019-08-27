from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox
from tkinter.ttk import Progressbar

import tkinter as tk
import train_and_test_model

class Application(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Etiquetado")
        self.iconbitmap('mining-icon.ico')
        self.resizable(0,0)
        self.geometry("485x385")

        #Tab
        self.tab_control = ttk.Notebook(self, width=480, height=355)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text='Entrenar')
        self.tab_control.add(self.tab2, text='Prueba')
        self.tab_control.grid(column=0, row=0, columnspan=3)

        #labels
        self.cor = ttk.Label(self.tab1, text="Correctos:", font=("Arial", 15))
        self.cor.grid(column=0, row=0)
        self.inc = ttk.Label(self.tab1, text="Incorrectos:", font=("Arial", 15))
        self.inc.grid(column=2, row=0)
        self.dud = ttk.Label(self.tab1, text="Dudosos:", font=("Arial", 15))
        self.dud.grid(column=4, row=0)
        self.lab = ttk.Label(self.tab1, text="Entrenando la red neuronal con", font=("Arial", 15))
        self.lab.grid(column=0, row=5,  columnspan=3)
        self.ll = ttk.Label(self.tab1, text="la data de Wikipedia", font=("Arial", 15))
        self.ll.grid(column=0, row=6,  columnspan=3)
        self.lab1 = ttk.Label(self.tab1, text="(Sólo simulación)", font=("Arial", 15))
        self.lab1.grid(column=0, row=7,  columnspan=2)
        self.exp = ttk.Label(self.tab2, text="Explicando lo que hace proyecto...", font=("Arial", 15))
        self.exp.grid(column=1, row=0, columnspan=2)
        self.etiq = ttk.Label(self.tab2, text="Etiquetas:", font=("Arial", 15))
        self.etiq.grid(column=1, row=2)
        self.resul = ttk.Label(self.tab2, text="El etiquetado", font=("Arial", 15))
        self.resul.grid(column=1, row=7, columnspan=100, rowspan=100)

        #Entrys
        self.txt = ttk.Entry(self.tab2,width=20)
        self.txt.grid(column=2, row=2)

        #Botones
        self.style = ttk.Style()
        self.style.configure('BW.TButton', foreground='white', background='blue')
        self.btn3 = ttk.Button(self.tab2, text="Comprobar", command=self.click, style="BW.TButton")
        self.btn3.grid(column=4, row=2, sticky='ns' , columnspan=2)
        self.btn2 = ttk.Button(self.tab1, text="Entrenar", style="BW.TButton", command=self.start)
        self.btn2.grid(column=4, row=5, sticky='ns')

        #Listbox
        #Lista de las etiquetas de prueba
        self.lbtab2 = tk.Listbox(self.tab2, highlightcolor="#0000ff", highlightbackground="#ff0000", selectbackground="#777")
        self.lbtab2.grid(column=2, row=4, columnspan=2)
        self.scrollbar1 = ttk.Scrollbar(self.tab2, orient=tk.VERTICAL, command=self.lbtab2.yview)
        self.scrollbar1.grid(column=3, row=4, sticky='ns')
        self.lbtab2.configure(yscrollcommand=self.scrollbar1.set)
        items = ( #aqui van los ítems por supuesto 
            "Python",
            "C",
            "C++",
            "Java",
            "Python",
            "C",
            "C++",
            "Java",
            "Python",
            "C",
            "C++",
            "Java"
        )
        self.lbtab2.insert(tk.END, *items)
        #lista de los correctos
        self.lbtab1 = tk.Listbox(self.tab1, highlightcolor="#0000ff", highlightbackground="#ff0000", selectbackground="#777")
        self.lbtab1.grid(column=0, row=2)
        self.scrollbar2 = ttk.Scrollbar(self.tab1, orient=tk.VERTICAL, command=self.lbtab1.yview)
        self.scrollbar2.grid(column=1, row=2, sticky='ns')
        self.lbtab1.configure(yscrollcommand=self.scrollbar2.set)
        items = ( 
            "Python",
            "C",
            "C++",
            "Java",
            "Python",
            "C",
            "C++",
            "Java",
            "Python",
            "C",
            "C++",
            "Java"
        )
        self.lbtab1.insert(tk.END, *items)

        #lista de los incorrectos
        self.lbtab2 = tk.Listbox(self.tab1, highlightcolor="#0000ff", highlightbackground="#ff0000", selectbackground="#777")
        self.lbtab2.grid(column=2, row=2)
        self.scrollbar3 = tk.Scrollbar(self.tab1, orient=tk.VERTICAL, command=self.lbtab2.yview)
        self.scrollbar3.grid(column=3, row=2, sticky='ns')
        self.lbtab2.configure(yscrollcommand=self.scrollbar3.set)
        items = ( 
            "Python",
            "C",
            "C++",
            "Java",
            "Python",
            "C",
            "C++",
            "Java",
            "Python",
            "C",
            "C++",
            "Java"
        )
        self.lbtab2.insert(tk.END, *items)

        #lista de los dudosos
        self.lbtab3 = tk.Listbox(self.tab1, highlightcolor="#0000ff", highlightbackground="#ff0000", selectbackground="#777")
        self.lbtab3.grid(column=4, row=2)
        self.scrollbar4 = tk.Scrollbar(self.tab1, orient=tk.VERTICAL, command=self.lbtab3.yview)
        self.scrollbar4.grid(column=5, row=2, sticky='ns')
        self.lbtab3.configure(yscrollcommand=self.scrollbar4.set)
        items = ( 
            "Python",
            "C",
            "C++",
            "Java",
            "Python",
            "C",
            "C++",
            "Java",
            "Python",
            "C",
            "C++",
            "Java"
        )
        self.lbtab3.insert(tk.END, *items)

        #Progressbar
        self.progress = ttk.Progressbar(self.tab1, orient="horizontal", length=200, mode="determinate")
        self.progress.grid(column=0, row=8, columnspan=3)

        self.pal = 0
        self.maxpal = 0

    #Eventos
    def start(self):
        self.progress["value"] = 0
        self.maxpal = 50000
        self.progress["maximum"] = 50000
        self.read()

    def read(self):
        self.pal += 500
        self.progress["value"] = self.pal
        if self.pal < self.maxpal:
            self.after(100, self.read)
        if self.pal == self.maxpal:
            self.cheat2 = ttk.Label(self.tab1, text="¡Entrenamiento exitoso!", font=("Arial", 15))
            self.cheat2.grid(column=1, row=11, rowspan=3, columnspan=3)

    def click(self):
        self.res = "El etiquetado " + self.txt.get() + " es (aqui va el resultado)"
        self.resul.configure(text= self.res)
        
app = Application()
app.mainloop()
