import tkinter as tk

def crear_ventana():
    ventana = tk.Tk()
    ventana.title("Mi Aplicación")
    ventana.geometry("400x300")

    etiqueta = tk.Label(ventana, text="¡Hola, mundo!")
    etiqueta.pack()

    boton = tk.Button(ventana, text="Cerrar", command=ventana.quit)
    boton.pack()

    ventana.mainloop()

crear_ventana()
