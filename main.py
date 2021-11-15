import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import pickle

class Coche:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

if __name__ == '__main__':
    listadoCoches = []

    # Creamos la interfaz
    ventana = tkinter.Tk()
    ventana.geometry("415x400")
    ventana.config(bg="aquamarine")
    # Le ponemos un titulo
    ventana.title("Interfaz Antonio Luis")

    # Creamos el label (titulo) y lo posicionamos en la columna 1 y la fila 0
    labelPrincipal = tkinter.Label(ventana, text ="Coches")
    labelPrincipal.grid(row = 0, column = 1)
    labelPrincipal.config(bg="aquamarine")
    # Creamos el label para la marca
    labelMarca = tkinter.Label(ventana, text ="Marca")
    labelMarca.grid(row = 1, column = 0)
    labelMarca.config(bg="aquamarine")
    # Creamos el texto correspondiente para la marca
    textoMarca = tkinter.Entry(ventana)
    textoMarca.grid(row = 1, column = 1)
    # Creamos el label para el modelo
    labelModelo = tkinter.Label(ventana, text="Modelo")
    labelModelo.grid(row = 2, column = 0)
    labelModelo.config(bg="aquamarine")
    # Creamos el texto correspondiente para el modelo
    textoModelo = tkinter.Entry(ventana)
    textoModelo.grid(row = 2, column = 1)
    # Creamos la tabla asignandole sus caracteristicas
    tabla = ttk.Treeview()
    tabla.grid(row=4, column=0, columnspan=3, ipadx=100)
    #Creamos un array para hacer las columnas
    tabla["column"] = ("1", "2")

    tabla.column("#0", width = 0)
    tabla.column("1", width=100, minwidth=100)
    tabla.column("2", width=100, minwidth=100)
    tabla.heading("1", text = "Marca")
    tabla.heading("2", text = "Modelo")

    #Creamos el fichero donde guardaremos los objetos
    fichero1 = open("ficheroCoches", "ab+")
    fichero1.seek(0)
    try:
        listadoCoches = pickle.load(fichero1)
    except:
        print("El fichero esta vacio")
    finally:
        fichero1.close()
    # Insertamos en el fichero el coche introducido manualmente
    for i in range(0, len(listadoCoches)):
        a: Coche = listadoCoches[i]
        tabla.insert("", i, i, text="", values=(a.marca, a.modelo))

    #Creamos el metodo añadir para introducir el objeto en el fichero
    def anadir():
        marca = textoMarca.get()
        modelo = textoModelo.get()
        a:Coche = Coche(marca, modelo)
        auxiliar:Coche = Coche("null", "null")
        #Controlamos que los campos no esten vacios
        if (marca != "" and modelo != ""):
            #Controlamos si el coche que queremos añadir existe
            for i in range (0, len(listadoCoches)):
                if(listadoCoches[i].marca == marca and listadoCoches[i].modelo==modelo):
                    auxiliar:Coche = listadoCoches[i]

            if (auxiliar.marca != marca or len(listadoCoches) == 0):

                for i in tabla.get_children():
                    tabla.delete(i)

                listadoCoches.append(a)

                for i in range (0, len(listadoCoches)):
                    a:Coche = listadoCoches[i]
                    tabla.insert("", i, i, text = "", values = (a.marca, a.modelo))
            else:
                messagebox.showinfo(title="Mensaje", message="Ya existe ese coche")

        else:
            messagebox.showinfo(title="Mensaje", message="Los campos no pueden esta vacios")

    botonAnadir = tkinter.Button(ventana, text ="Añadir", command = anadir)
    botonAnadir.place(x = 50, y = 300)
    botonAnadir.config(bg="AntiqueWhite4")

    # Creamos el metodo modificar para modificar el objeto seleccionado
    def modificar():
        marca = textoMarca.get()
        modelo = textoModelo.get()
        a: Coche = Coche(marca, modelo)
        auxiliar: Coche = Coche("null", "null")

        if (marca != "" and modelo != ""):
            # Controlamos si el coche que queremos modificar existe
            for i in range(0, len(listadoCoches)):
                if (listadoCoches[i].marca == marca):
                    listadoCoches[i].modelo = modelo
                    listadoCoches[i].marca = marca
                    auxiliar: Coche = listadoCoches[i]

            if (auxiliar.marca == marca):

                for i in tabla.get_children():
                    tabla.delete(i)

                for i in range(0, len(listadoCoches)):
                    a: Coche = listadoCoches[i]
                    tabla.insert("", i, i, text="", values=(a.marca, a.modelo))
            else:
                messagebox.showinfo(title="Mensaje", message="No existe ese coche")
        else:
            messagebox.showinfo(title="Mensaje", message="Introduce todos los datos")

    botonMod = tkinter.Button(ventana, text="Modificar", command = modificar)
    botonMod.place(x = 150, y = 300)
    botonMod.config(bg="AntiqueWhite4")

    # Creamos el metodo borrar para borrar el objeto seleccionado
    def borrar():
        try:
            item = tabla.selection()[0]
            marca = tabla.item(item, option="values")[0]

            for i in range(len(listadoCoches) - 1, -1, -1):
                a: Coche = listadoCoches[i]
                if (a.marca == marca):
                    listadoCoches.remove(a)

            tabla.delete(item)
        except:
            messagebox.showinfo("Mensaje", "Selecciona la fila que deseas borrar")

    botonBorrar = tkinter.Button(ventana, text ="Borrar", command = borrar)
    botonBorrar.place(x = 270, y = 300)
    botonBorrar.config(bg="red")

    # Cuando cerremos la ventana se cerrará la escritura en el fichero
    def on_closing():
        fichero = open("ficheroCoches", "wb")
        pickle.dump(listadoCoches, fichero)
        fichero.close()
        ventana.destroy()

    ventana.protocol("WM_DELETE_WINDOW", on_closing)
    ventana.mainloop()