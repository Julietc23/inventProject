from tkinter import *
import sqlite3

    #   funciones:
#funcion para guardar lo que escribe: 
def guardar():
    global usuario
    global contraseña
    usuario = usuarioE.get()
    contraseña = contraseñaE.get()

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
