from tkinter import *
import sqlite3

    #   funciones:
#funcion para guardar lo que escribe:
def guardar():
    global usuario
    global contraseña
    usuario = usuarioE.get()
    contraseña = contraseñaE.get()


    #print(f"usuario:{usuario}, contraseña:{contraseña}");
    
                #BASE DE DATOS

conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

#creacion de tabla y datos

        #creacion de tabla
try:
    cursor.execute("""
        CREATE TABLE usuarios (
            usuario VARCHAR(100) UNIQUE NOT NULL,
            contraseña VARCHAR(100) UNIQUE NOT NULL
                   )
    """)
    cursor.executemany("INSERT INTO usuarios VALUES (?,?)")
except:
    pass



conexion.commit()

    #consulta de datos:

cursor.execute("SELECT * FROM usuarios")
usuarios_registrados = cursor.fetchall()



conexion.close()




                #INTERFAZ

root = Tk()

usuario=StringVar()
contraseña=StringVar()

#configuracion de la raiz:
root.config(bd="15")
root.geometry("600x500")
root.resizable(0,0)

#configuracion del frame "iniciar sesión"
frame = Frame(root)
frame.config(bg="#b9b9b9", width=300, height=450, bd="15")
frame.place(relx=0.5, rely=0.5, anchor="center")
frame.pack_propagate(False)


#labels y entry en frame:
    #   text "Log in"
Label(frame, 
      text="LOG IN",
      bg="#b9b9b9",
      font=("Helvetica", 20, "bold"),
      fg="#3D3D3D"
      ).pack()

    #   text "usuario" y entry:
Label(frame,
      text="Usuario:",
      bg="#b9b9b9",
      font=("Helvetica", 10, "bold"),
      fg="#3D3D3D",
      justify="left"
      ).pack(fill="both")

usuarioE = Entry(frame,justify="center",bd="15")
usuarioE.pack(fill="both")

    #   text "contraseña" y entry:
Label(frame,
      text="Contraseña:",
      bg="#b9b9b9",
      font=("Helvetica", 10, "bold"),
      fg="#3D3D3D",
      justify="left"
      ).pack(fill="both")

contraseñaE = Entry(frame,justify="center",bd="15")
contraseñaE.pack(fill="both")
contraseñaE.config(show="*")

    # label button:
labelBut = Label(frame,padx=20,pady=20,bg="#b9b9b9",bd="15")
labelBut.pack()
logBut = Button(labelBut, text="Log in",command=guardar)
logBut.pack()

root.mainloop()








def guardar_datos():
    # Recuperar los datos de los campos de entrada
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()
    
    if usuario and contrasena:  # Verificar que no estén vacíos
        # Insertar datos en la base de datos
        cursor.execute('INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)', (usuario, contrasena))
        conexion.commit()  # Confirmar los cambios
        
        # Limpiar los campos de entrada
        entry_usuario.delete(0, tk.END)
        entry_contrasena.delete(0, tk.END)
        
        print("Datos guardados correctamente")
    else:
        print("Por favor, ingrese ambos campos")