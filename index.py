import sqlite3              #productos - 
from tkinter import *

conexion = sqlite3.connect("productos.db")
cursor = conexion.cursor()

# try:
#     cursor.execute("""
#         CREATE TABLE productos (
#         id INTEGER, 
#         nombre VARCHAR(100) NOT NULL,
#         marca VARCHAR(100) NOT NULL,
#         precio INTEGER
#                    )
#     """)
    
# except sqlite3.OperationalError:
#     print("la base de datos ya existe")


cursor.execute("INSERT INTO productos VALUES (1,'mayonesa','hellmans',1500)")

producto1 = cursor.fetchall() 
print(producto1)



conexion.commit()
conexion.close()





