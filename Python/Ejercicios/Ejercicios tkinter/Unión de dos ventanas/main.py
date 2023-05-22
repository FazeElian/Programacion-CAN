import tkinter as tk
from tkinter import ttk

def abrir_ventana_secundaria():
  # Crear una ventana secundaria.
  ventana_secundaria = tk.Toplevel()
  ventana_secundaria.title("Encuesta en proceso")  #Titulo de ventana secundaria
  ventana_secundaria.configure(width=400, height=400)

# Formulario Ventana 2
  # Crear los widgets del formulario
  tk.Label(ventana_secundaria,
           text="¿Como conociste nuestra empresa?").grid(row=0, column=0)
  conocimiento_empresa = tk.Entry(ventana_secundaria)
  conocimiento_empresa.grid(row=0, column=1)

  tk.Label(ventana_secundaria,
           text="¿Te gustan nuestros productos?").grid(row=1, column=0)
  gusto_productos = tk.Entry(ventana_secundaria)
  gusto_productos.grid(row=1, column=1)

  tk.Label(ventana_secundaria, text="¿Has comprado en nuestra tienda?").grid(row=2, column=0)
  compra = tk.Entry(ventana_secundaria)
  compra.grid(row=2, column=1)

  tk.Label(ventana_secundaria,
text="¿Recomendarías nuestros productos?").grid(row=2, column=0)
  recomendacion = tk.Entry(ventana_secundaria)
  recomendacion.grid(row=2, column=1)

  # Crear un botón dentro de la ventana secundaria
  boton_enviar = tk.Button(ventana_secundaria, text="Enviar Encuesta")
  boton_enviar.grid(row=10, column=-1, columnspan=2, pady=100)
  
  # para cerrar la misma:
  boton_cerrar = ttk.Button(ventana_secundaria,
  text="Cerrar ventana",
  command=ventana_secundaria.destroy)
  boton_cerrar.place(x=75, y=75)
  boton_cerrar.grid(row=10, column=2, columnspan=2, pady=100)


# Crear la ventana principal.
index_ventana = tk.Tk()
index_ventana.config(width=1000, height=1000)
index_ventana.title("Pàgina Inicio")
bienvenida = tk.Label(index_ventana, text="¡Bienvenido al programa! Para realizar la encuesta da clic en el botón: ")
bienvenida.pack(pady=20)

# Texto de Bienvenida de ventana principal
bienvenida = tk.Label(index_ventana, text="¡Bienvenido al programa! Para realizar la encuesta da clic en el botón: ")
bienvenida.pack(pady=20)



# abrir_ventana_secundaria().
boton_abrir = ttk.Button(index_ventana, text="Realizar Encuesta -->", command=abrir_ventana_secundaria)
boton_abrir.place(x=130, y=100)
index_ventana.mainloop()