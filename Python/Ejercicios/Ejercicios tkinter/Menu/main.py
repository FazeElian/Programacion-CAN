import tkinter as tk

ventana = tk.Tk()  #Tkinter de ventana
ventana.title("Ventana Menu")
ventana.configure(bg = "gray")
ventana.geometry("700x300")

menu = tk.Menu()  #Tkinter de ventana de menu

#Opciones de menu
menu_inicio = tk.Menu(menu, tearoff=0)
menu_categorias = tk.Menu(menu, tearoff=0)
menu_productos = tk.Menu(menu, tearoff=0)
menu_carrito = tk.Menu(menu, tearoff=0)

#Agregar las opciones de menu
menu.add_cascade(label="Inicio", menu=menu_inicio)
menu.add_cascade(label="Categorìas", menu=menu_categorias)
menu.add_cascade(label="Productos", menu=menu_productos)
menu.add_cascade(label="Carrito de Compras", menu=menu_carrito)

#Creaciòn subopciones de Categorias
menu_categorias.add_command(label="Tecnologìa")
menu_categorias.add_command(label="Electrodomèsticos")
menu_categorias.add_command(label="Computadores")
menu_categorias.add_command(label="Celulares")
menu_categorias.add_command(label="Perifèricos")
menu_categorias.add_command(label="Monitores")
menu_categorias.add_command(label="Memorias USB")
menu_categorias.add_command(label="Tarjetas SD")

#Creaciòn subopciones de Productos
menu_productos.add_command(label="Mis productos")
menu_productos.add_command(label="Mis Compras")
menu_productos.add_command(label="Mis Favoritos")

#Creaciòn subopciones de Inicio
menu_inicio.add_command(label="Mi Cuenta")
menu_inicio.add_command(label="Ajustes")
menu_inicio.add_command(label="Cerrar Sesión")

#Creaciòn subopciones de Carrito
menu_carrito.add_command(label="Añadir productos")
menu_carrito.add_command(label="Ir a carrito de compras")
menu_carrito.add_command(label="Continuar Compra")

#Mostrar barra de menù
ventana.config(menu=menu)

#Designar pantalla principal
ventana.mainloop()