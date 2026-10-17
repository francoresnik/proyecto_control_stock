import mysql.connector
#importamos las librerias de mysql

conexion = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password ="admin",
    database ="control_stock"
)

def mostrar_productos():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    for producto in productos:
        print(
            f"ID: {producto[0]} | "
            f"Producto: {producto[1]} | "
            f"Precio: {producto[2]} | "
            f"Clase: {producto[3]} | "
            f"Cantidad: {producto[4]}"
        )




def añadir_producto():
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    clase = input("Clase del producto: ")
    cantidad = int(input("Cantidad disponible: "))

    cursor = conexion.cursor() #nuevamente, se crea el objeto que se comunique
    #con mysql

    consulta = """
    INSERT INTO productos (nombre, precio, clase, cantidad)
    VALUES (%s, %s, %s, %s)
    """
    #usamos el %s como un indicador de posicion, cuando se haga la consulta
    #se va a cambiar por los valores que queremos añadir

    valores = (nombre, precio, clase, cantidad)

    cursor.execute(consulta, valores)
    conexion.commit() #commit actualiza los valores, hace la conexion
    #con mysql y los guarda, ya estamos guardando datos

    cursor.close()
    print("Producto añadido correctamente")


def eliminar_producto():

    identificador = int(input("Escriba la id del producto a eliminar: "))
    
    eliminar = """
    DELETE FROM PRODUCTOS WHERE ID = %s"""

    cursor = conexion.cursor()
    cursor.execute(eliminar,(identificador,))
    print(cursor.rowcount)
    conexion.commit()

    cursor.close()
    print("elemento eliminado correctamente")
