from tkinter import ttk
from tkinter import Menu
from tkinter import Text
from tkinter import messagebox as MessageBox
from tkinter import filedialog as FileDialog
from tkinter.ttk import Progressbar

import tkinter as tk
from train_and_test_model import *

class Application(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Etiquetado")
        #self.iconbitmap('mining-icon.ico') #Para SO Windows
        #self.iconbitmap('@~/red_neuronal/mining-icon.xbm') #Para SO Linux
        self.resizable(0,0)
        self.geometry("585x450")
        self.s = ttk.Style()
        self.s.configure('My.TFrame', background='#9bdba3')

        #colores
        

        #Tab
        self.tab_control = ttk.Notebook(self, width=580, height=420)
        self.tab1 = ttk.Frame(self.tab_control, style="My.TFrame")
        self.tab2 = ttk.Frame(self.tab_control, style="My.TFrame")
        self.tab_control.add(self.tab1, text='Entrenar')
        self.tab_control.add(self.tab2, text='Prueba')
        self.tab_control.grid(column=0, row=0, columnspan=3)

        #labels tab1
        self.cor = ttk.Label(self.tab1, background="#9bdba3", text="Correctos:", font=("Arial", 15))
        self.cor.grid(column=0, row=0)

        self.inc = ttk.Label(self.tab1, background="#9bdba3", text="Incorrectos:", font=("Arial", 15))
        self.inc.grid(column=2, row=0)

        self.dud = ttk.Label(self.tab1, background="#9bdba3", text="Dudosos:", font=("Arial", 15))
        self.dud.grid(column=4, row=0)

        #Espacio en blanco
        self.espacio1 = ttk.Label(self.tab1, background="#9bdba3", text="")
        self.espacio1.grid(column=1, row=6)

        self.lab = ttk.Label(self.tab1, background="#9bdba3", text="Entrenando la red neuronal con", font=("Arial", 15))
        self.lab.grid(column=1, row=7, columnspan=3)

        self.ll = ttk.Label(self.tab1, background="#9bdba3", text="la data de los Boletines", font=("Arial", 15))
        self.ll.grid(column=1, row=8, columnspan=3)

        self.lab1 = ttk.Label(self.tab1, background="#9bdba3", text="(Sólo simulación)", font=("Arial", 15))
        self.lab1.grid(column=1, row=9, columnspan=3)

        #Espacio en blanco
        self.espacio2 = ttk.Label(self.tab1, background="#9bdba3", text="")
        self.espacio2.grid(column=1, row=10)

        #Label Paths
        self.lab1 = ttk.Label(self.tab1, background="#9bdba3", text="Ruta del Documento: ", font=("Arial", 12))
        self.lab1.grid(column=0, row=12)

        #Entry Paths Documents
        self.entry = ttk.Entry(self.tab1, width=30)
        self.entry.grid(column=2, row=12)
        self.entry.focus()
        self.entry.insert(0,"boletines/boletines1.csv")

        #Espacio en blanco
        self.espacio3 = ttk.Label(self.tab1, background="#9bdba3", text="")
        self.espacio3.grid(column=1, row=13)

        #Progressbar
        self.progress = ttk.Progressbar(self.tab1, orient="horizontal", length=200, mode="determinate")
        self.progress.grid(column=1, row=14, columnspan=3)

        #labels tab2
        self.exp = ttk.Label(self.tab2, background="#9bdba3", text="Explicando lo que hace proyecto...", font=("Arial", 15))
        self.exp.grid(column=1, row=0, columnspan=2)

        self.etiq = ttk.Label(self.tab2, background="#9bdba3", text="Etiquetas:", font=("Arial", 15))
        self.etiq.grid(column=0, row=2)

        #Entrys
        self.txt = Text(self.tab2)
        self.txt.grid(column=2, row=2)
        self.txt.config(width=30, height=3)

        #Botones Estilo
        self.style = ttk.Style()
        self.style.configure('BW.TButton', foreground='black', background='#9aadbf')

        #Botones tab1
        self.btn2 = ttk.Button(self.tab1, text="Entrenar", style="BW.TButton", command=self.start)
        self.btn2.grid(column=4, row=12, sticky='ns')

        self.btn2 = ttk.Button(self.tab1, text="Cargar Modelo", style="BW.TButton", command=self.load_model)
        self.btn2.grid(column=4, row=8, sticky='ns')

        #Espacio en blanco
        self.espacio4 = ttk.Label(self.tab2, background="#9bdba3", text="")
        self.espacio4.grid(column=5, row=2)

        #Espacio en blanco
        self.espacio5 = ttk.Label(self.tab2, background="#9bdba3", text="")
        self.espacio5.grid(column=8, row=2)

        #Botones tab2
        self.btn3 = ttk.Button(self.tab2, text="Comprobar", command=self.click, style="BW.TButton")
        self.btn3.grid(column=10, row=2, sticky='ns')


        #lista de los correctos
        self.lbtab1 = tk.Listbox(self.tab1, highlightcolor="#0000ff", highlightbackground="#ff0000", selectbackground="#777")
        self.lbtab1.grid(column=0, row=2)
        self.scrollbar2 = ttk.Scrollbar(self.tab1, orient=tk.VERTICAL, command=self.lbtab1.yview)
        self.scrollbar2.grid(column=1, row=2, sticky='ns')
        self.lbtab1.configure(yscrollcommand=self.scrollbar2.set)

        #lista de los incorrectos
        self.lbtab2 = tk.Listbox(self.tab1, highlightcolor="#0000ff", highlightbackground="#ff0000", selectbackground="#777")
        self.lbtab2.grid(column=2, row=2)
        self.scrollbar3 = tk.Scrollbar(self.tab1, orient=tk.VERTICAL, command=self.lbtab2.yview)
        self.scrollbar3.grid(column=3, row=2, sticky='ns')
        self.lbtab2.configure(yscrollcommand=self.scrollbar3.set)
        

        #lista de los dudosos
        self.lbtab3 = tk.Listbox(self.tab1, highlightcolor="#0000ff", highlightbackground="#ff0000", selectbackground="#777")
        self.lbtab3.grid(column=4, row=2)
        self.scrollbar4 = tk.Scrollbar(self.tab1, orient=tk.VERTICAL, command=self.lbtab3.yview)
        self.scrollbar4.grid(column=5, row=2, sticky='ns')
        self.lbtab3.configure(yscrollcommand=self.scrollbar4.set)

        self.pal = 0
        self.maxpal = 0

    #Eventos
    def start(self):
        self.entry.delete(0, tk.END)
        file_dic = FileDialog.askopenfile(title="Abrir el Boletin")
        self.entry.insert(0, file_dic.name)
        self.progress["value"] = 0
        self.maxpal = 1500
        self.read()
        self.progress["maximum"] = 1500


    def read(self):
        self.pal += 500
        self.progress["value"] = self.pal
        if self.pal < self.maxpal:
            self.after(100, self.read)
        if self.pal == self.maxpal:
            #Model
            entry = self.entry.get()
            document = read_doc(entry)
            self.doc = document
            self.model = train_model(document)

            #List Incorrectos
            incorrectos = document[document.Supervision == 1]
            items = incorrectos['ID'][:]
            self.lbtab2.insert(tk.END, *items)

            #List Correctos
            correctos = document[document.Supervision == 0]
            items = correctos['ID'][:]
            self.lbtab1.insert(tk.END, *items)

            #List Dusosos
            dudosos = document[document.Supervision == 3]
            items = dudosos['ID'][:]
            self.lbtab3.insert(tk.END, *items)

            #Botones tab1
            self.btn4 = ttk.Button(self.tab1, text="Guardar", style="BW.TButton", command=self.save_model)
            self.btn4.grid(column=4, row=14, sticky='ns')

            self.cheat2 = ttk.Label(self.tab1, text="¡Entrenamiento exitoso!", font=("Arial", 15))
            self.cheat2.grid(column=1, row=16, columnspan=3)

    def save_model(self):
        paths = FileDialog.askdirectory(title="Seleccionar Directorio del Respaldo") + '/'
        save_model(paths, self.model, self.doc)
        MessageBox.showinfo('Información','El modelo de entramiento\nse ha almacenado con éxito.')

    def load_model(self):
        #Model
        paths = FileDialog.askdirectory(title="Abrir Directorio del Respaldo") + '/'
        load_files = load_model(paths)
        document = load_files[2]
        self.model = load_files

        #List Incorrectos
        incorrectos = document[document.Supervision == 1]
        items = incorrectos['ID'][:]
        self.lbtab2.insert(tk.END, *items)

        #List Correctos
        correctos = document[document.Supervision == 0]
        items = correctos['ID'][:]
        self.lbtab1.insert(tk.END, *items)

        #List Dusosos
        dudosos = document[document.Supervision == 3]
        items = dudosos['ID'][:]
        self.lbtab3.insert(tk.END, *items)

        MessageBox.showinfo('Información','El modelo de entramiento\nse ha cargado con éxito.')


    def click(self):
        paragraph = self.txt.get("1.0", "end-1c")
        prediction = test_model(paragraph, self.model)
        MessageBox.showinfo('Información', 'El texto de prueba que ha\nintroducido es: ' + prediction)
        self.txt.delete("1.0", "end-1c")
        
app = Application()
app.mainloop()
