import os
from dotenv import load_dotenv

load_dotenv()

import mysql.connector
#importamos las librerias de mysql

conexion = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password=os.getenv("DB_PASSWORD"),
    database ="control_stock"
)

def mostrar_productos():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    cursor.close()

    return productos

def añadir_producto(nombre=None, precio=None, clase=None, cantidad=None):

    if nombre is None:
        nombre = input("Nombre del producto: ")

    if precio is None:
        precio = float(input("Precio del producto: "))

    if clase is None:
        clase = input("Clase del producto: ")

    if cantidad is None:
        cantidad = int(input("Cantidad disponible: "))

    cursor = conexion.cursor()

    consulta = """
    INSERT INTO productos (nombre, precio, clase, cantidad)
    VALUES (%s, %s, %s, %s)
    """

    valores = (nombre, precio, clase, cantidad)

    cursor.execute(consulta, valores)
    conexion.commit()

    cursor.close()
    print("Producto añadido correctamente")


def eliminar_producto(iid=None):
    if iid is None:
        identificador = int(input("Escriba la id del producto a eliminar: "))
    else:
        identificador = int(iid)
    
    eliminar = """
    DELETE FROM PRODUCTOS WHERE ID = %s"""

    cursor = conexion.cursor()
    cursor.execute(eliminar,(identificador,))
    conexion.commit()

    cursor.close()
    print("elemento eliminado correctamente")
