import tkinter
from tkinter import *
import sqlite3
from tkinter import messagebox as MessageBox
from tkinter import ttk


def escribir():
    dni = caja1.get()
    gmail = caja2.get()
    nombre_de_usuario = caja3.get()
    numero_telf = caja4.get()
    print(dni, gmail, nombre_de_usuario, numero_telf)
    
    
    sql='''INSERT INTO login (DNI, Gmail, Nombre_Usu, Num_Telf)
    VALUES('{}', '{}', '{}', '{}')'''.format(dni, gmail, nombre_de_usuario, numero_telf)
    cur.execute(sql)
    bd.commit()
    bd.close()

def buscar():
    dni = lista_desplegable.get()
    print(dni)
    query = "SELECT * FROM login WHERE DNI ={}".format(dni)
    print(query)
    cur.execute(query)
    datos = cur.fetchall()
    print(datos)
    
    caja1.insert(0, datos[0][0])
    caja2.insert(0, datos[0][1])
    caja3.insert(0, datos[0][2])
    caja4.insert(0, datos[0][3])

def borrar():
    
    caja1.delete(0,END)
    caja2.delete(0,END)
    caja3.delete(0,END)
    caja4.delete(0,END)
    
    
bd = sqlite3.connect("lemalogin.bd")
cur = bd.cursor()
cur.execute("SELECT DNI FROM login")
resp = cur.fetchall()    

ventana = Tk()
ventana.title ("Inf Pers")
ventana.geometry ("350x200+500+250")
ventana.config(bg = "black")
ventana.resizable(0,0)
Label(ventana, text = "DNI:", bg = "chartreuse").pack()
caja1 = Entry(ventana)
caja1.pack()
Label(ventana, text = "Gmail:", bg = "chartreuse").pack()
caja2 = Entry(ventana)
caja2.pack()
Label(ventana, text = "Nombre de Usuario:", bg = "chartreuse").pack()
caja3 = Entry(ventana)
caja3.pack()
Label(ventana, text = "Numero Telf:", bg = "chartreuse").pack()
caja4 = Entry(ventana)
caja4.pack()

boton = tkinter.Button (ventana, text= "Buscar", command = buscar, bg="chartreuse")
boton.pack()
boton.place(x=270, y=169)

boton = tkinter.Button (ventana, text= "Guardar", command = escribir, bg="chartreuse")
boton.pack()
boton.place(x=10, y=169)

boton = tkinter.Button (ventana, text= "Borrar", command = borrar, bg="chartreuse")
boton.pack()
boton.place(x=15, y=50)

#LISTA DESPLEGABLE
lista_desplegable = ttk.Combobox(ventana,width=17)
lista_desplegable.place (x=100, y=169)

opciones = ["opcion 1","opcion 2","opcion 3",]
lista_desplegable['values']=resp



#Acceder a base de datos



#cursor.execute("SELECT * FROM login")
#print(cursor)
#datos = cursor.fetchall()
#print(datos)

#bd.commit()



#def login(self):

ventana.mainloop()
