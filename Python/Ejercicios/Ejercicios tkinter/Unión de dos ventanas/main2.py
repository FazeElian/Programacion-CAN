import tkinter as tk
from tkinter import ttk

# Crear la ventana principal.
ventana1 = tk.Tk()
ventana1.geometry("500x300")
ventana1.title("Página Inicio - Responde la encuesta")

# Texto de Bienvenida de ventana principal
bienvenida = tk.Label(ventana1, text="¡Bienvenido al programa! Para realizar la encuesta da clic en el botón: ")
bienvenida.pack(pady=20)

def abrir_ventana2():
  # Crear una ventana secundaria.
  ventana2 = tk.Toplevel()
  ventana2.title("Encuesta en proceso")  #Titulo de ventana secundaria
  ventana2.geometry("500x300")

# Formulario Ventana 2
  # Crear los widgets del formulario
  tk.Label(ventana2, text="¿Como conociste nuestra empresa?").grid(row=0, column=0)
  conocimiento_empresa = tk.Entry(ventana2)
  conocimiento_empresa.grid(row=0, column=1)

  tk.Label(ventana2, text="¿Te gustan nuestros productos?").grid(row=1, column=0)
  gusto_productos = tk.Entry(ventana2)
  gusto_productos.grid(row=1, column=1)

  tk.Label(ventana2, text="¿Has comprado en nuestra tienda?").grid(row=2, column=0)
  compra = tk.Entry(ventana2)
  compra.grid(row=2, column=1)

  tk.Label(ventana2, text="¿Recomendarías nuestros productos?").grid(row=2, column=0)
  recomendacion = tk.Entry(ventana2)
  recomendacion.grid(row=2, column=1)

  # Crear un botón dentro de la ventana secundaria
  boton_enviar = tk.Button(ventana2, text="Enviar Encuesta", command=encuesta_enviada)
  boton_enviar.grid(row=10, column=0, columnspan=2, pady=100)
  
  # para cerrar la misma:
  boton_cerrar = ttk.Button(ventana2, text="Cerrar ventana", command=ventana2.destroy)
  boton_cerrar.place(x=75, y=75)
  boton_cerrar.grid(row=10, column=2, columnspan=2, pady=100)

def encuesta_enviada ():
  # Crear una ventana de confirmación de envío
  encuesta_enviada = tk.Toplevel()
  encuesta_enviada.title("Encuesta enviada con éxito")  
  encuesta_enviada.geometry("500x300")
  tk.Label(encuesta_enviada, text="Encuesta enviada con éxito").grid(row=0, column=0)

# abrir_ventana2().
boton_abrir = ttk.Button(ventana1, text="Realizar Encuesta -->", command=abrir_ventana2)
boton_abrir.place(x=185, y=100)
ventana1.mainloop()