import tkinter as tk #Importar tk kinter, ventana
from elements import Elements #Importar archivo "Elements"


length = 117 #Longitud Ventana

window = tk.Tk() #Tk
window.title('Top 10 Mejores Jugadores de Fútbol') #Título de Ventana
window.config(bg="gray12") #Color fondo de ventana

label = tk.Label(text="¿Qué jugador del Top 10 quieres buscar?") #Texto Pregunta
label.grid(row='2', column='9') #Ubicación por filas y columnas de texto Pregunta (también margen superior)
Elementneeded = tk.Entry(width=80) #Largo Cuadro para escribir
Elementneeded.grid(row='3', column='9') #Ubicación por filas y columnas de texto Pregunta (también margen superior)
Text_box = tk.Text(height='10', width='120', wrap='word') #Largo y Ancho del cuadro donde aparece la info al buscar
Text_box.grid(row='8', column='9', columnspan='1') #Ubicación por filas y columnas de cuadro de info (también margen superior)


def Clearbox(): #Definición de variable "Clearbox" (variable fija)
    Text_box.delete('1.0', 'end')
    Elementneeded.delete(0, 'end')
    Stringvar.set('None')


Num = 0


def Next(self):
    global Num
    global Stringvar
    try:
        Num = list(Elements).index(Elementneeded.get().lower()) #Definición variable "Num" y su contenido
        if Num == length: #Condicional: Si "Num" es igual a "length" Hacer:
            Num = 0 #Num es igual a cero
            Index = list(Elements.keys())[Num] #Definición de lista de contenido en: "Elements", este fue un documento ya creado
            Elementneeded.delete(0, 'end')
            Elementneeded.insert(0, Index)
            Newindex = Elements[Index]
            Text_box.delete('1.0', 'end')
            Text_box.insert('1.0', Newindex)
            Stringvar.set(Elementneeded.get().lower())

        else: #Condicional: Sino, Hacer: 
            Num = Num + 1 #Sino "Num" será igual a ese número = Num numado o aumentado en 1 (contador)
            Index = list(Elements.keys())[Num]
            Elementneeded.delete(0, 'end')
            Elementneeded.insert(0, Index)
            Newindex = Elements[Index]
            Text_box.delete('1.0', 'end')
            Text_box.insert('1.0', Newindex)
            Stringvar.set(Elementneeded.get().lower())
    except: #Excepto que:
        Text_box.delete('1.0', 'end')
        Text_box.insert(
            '1.0',
            'You can not move through elements if no valid element is selected' #Texto que saldrá con el "excepto"
        )


def Back(self):
    global Stringvar
    global Num
    try:

        Num = list(Elements).index(Elementneeded.get().lower())
        if Num == 0:
            Num = length
            Index = list(Elements.keys())[Num]
            Elementneeded.delete(0, 'end')
            Elementneeded.insert(0, Index)
            Newindex = Elements[Index]
            Text_box.delete('1.0', 'end')
            Text_box.insert('1.0', Newindex)
            Stringvar.set(Elementneeded.get().lower())
        else:
            Num = Num - 1
            Index = list(Elements.keys())[Num]
            Elementneeded.delete(0, 'end')
            Elementneeded.insert(0, Index)
            Newindex = Elements[Index]
            Text_box.delete('1.0', 'end')
            Text_box.insert('1.0', Newindex)
            Stringvar.set(Elementneeded.get().lower())
    except:
        Text_box.delete('1.0', 'end')
        Text_box.insert(
            '1.0',
            'You can not move through elements if no valid element is selected'
        )





def callback(selection):
    Text_box.delete('1.0', 'end')
    Text_box.insert('1.0', Elements[selection])
    Elementneeded.delete(0, 'end')
    Elementneeded.insert(0, selection)


def Search(self):
    global Stringvar
    Text_box.delete('1.0', 'end')
    try:
        Text_box.insert('1.0', Elements[Elementneeded.get().lower()])
        Stringvar.set(Elementneeded.get().lower())
    except:
        Text_box.insert('1.0', 'That is not an element')


Stringvar = tk.StringVar(window, 'None')
Dropdown.grid(row='2', column='300', columnspan='2')
Clear = tk.Button(text="Clear", command=Clearbox)
Clear.grid(row='3', padx='500', column='300')
window.bind('<Return>', Search)
window.bind('<Right>', Next)
window.bind('<Left>', Back)
window.mainloop()
