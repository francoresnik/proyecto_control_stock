#-------------CONEXIONES-----------------
import conexion
import tkinter as tk
from tkinter import ttk
from dotenv import load_dotenv
from tkinter import messagebox



ventana = tk.Tk()
ventana.title("Sistema de gestión")
ventana.geometry("800x500")
ventana.configure(bg="#20252d")

#-----------------FUNCIONES---------------------

def mostrar_menu():
    pantalla_inicio.pack_forget()
    pantalla_menu.pack()

def borrar_producto():
    pantalla_menu.pack_forget()
    pantalla_eliminar.pack()
    


def volver_menu():
    pantalla_consulta.pack_forget()
    pantalla_menu.pack()

def volver_inicio():
    pantalla_menu.pack_forget()
    pantalla_inicio.pack()

def consultar_producto():
    pantalla_menu.pack_forget()
    pantalla_consulta.pack()

    # Limpiar la tabla
    for fila in tabla_productos.get_children():
        tabla_productos.delete(fila)

    # Obtener productos de MySQL
    productos = conexion.mostrar_productos()

    # Insertar productos en la tabla
    for producto in productos:
        tabla_productos.insert(
            "",
            "end",
            iid=str(producto[0]),
            values=(producto[1], producto[2], producto[4], producto[3])
        )
    
def salir_programa():
    ventana.destroy()

def ingresar_producto():
    pantalla_menu.pack_forget()
    pantalla_ingresar_productos.pack()

def mostrar_info():
    nombre = entrada_nombre.get().strip()

    if nombre == "":
        resultado.config(text="ERROR: debe ingresar un nombre")
        return

    try:
        precio = float(entrada_precio.get())
    except ValueError:
        resultado.config(text="Error: No es un precio válido")
        return

    if precio <= 0:
        resultado.config(text="El precio debe ser mayor a cero")
        return

    try:
        cantidad = int(entrada_cantidad.get())
    except ValueError:
        resultado.config(text="Error: No es una cantidad válida")
        return

    if cantidad < 0:
        resultado.config(text="La cantidad no puede ser negativa")
        return

    categoria = entrada_categoria.get().strip()

    if categoria == "":
        resultado.config(text="ERROR: Debe seleccionar una categoría")
        return

    conexion.añadir_producto(nombre, precio, categoria, cantidad)

    resultado.config(text="¡Producto guardado correctamente!")

def eliminar_producto_tk():
    id_producto = entrada_eliminar.get()
    
    if id_producto.strip() == "":
        messagebox.showwarning(
            "ATENCION",
            "debes seleccionar un producto para eliminar"
        )
        return
    
    try:
        id_producto = int(id_producto)

    except ValueError:
        messagebox.showwarning(
            "Error",
            "La ID debe ser un número entero"
        )
        return


    confirmacion = messagebox.askyesno(
        "confirmar eliminacion?",
        "estas seguro que quieres eliminar esto?"
    )
    if confirmacion:

        conexion.eliminar_producto(id_producto)

        entrada_eliminar.delete(0, tk.END)

def volver_menu(pantalla_actual):
    pantalla_actual.pack_forget()
    pantalla_menu.pack()

#-----------------PANTALLAS----------------------
# Primera pantalla
pantalla_inicio = tk.Frame(ventana, bg="#20252d")

titulo = tk.Label(
    pantalla_inicio,
    text="Pantalla de inicio",
    bg="#20252d",
    fg="white"
)

titulo.grid(row=0, column=0, padx=10, pady=10)

# Segunda pantalla
pantalla_menu = tk.Frame(ventana, bg="#20252d")

texto_menu = tk.Label(
    pantalla_menu,
    text="Menú principal",
    width= 22,
    height=2,
    bg="#20252d",
    fg="white"
)
texto_menu.grid(row=0, column=0, columnspan=4, pady=20)

#pantalla consulta

pantalla_consulta = tk.Frame(ventana, bg="#20252d")

texto_consulta = tk.Label(
    pantalla_consulta,
    text= "consultar productos",
    font=("Arial", 12),
    bg="#20252d",
    fg="white",
    width= 22,
    height=2,
)
texto_consulta.grid(row=0, column=2, pady=20)

tabla_productos = ttk.Treeview(
    pantalla_consulta,
    columns=("nombre", "precio", "cantidad", "categoria"),
    show="headings"
)

tabla_productos.heading("nombre", text="Nombre")
tabla_productos.heading("precio", text="Precio")
tabla_productos.heading("cantidad", text="Cantidad")
tabla_productos.heading("categoria", text="Categoría")

tabla_productos.column("nombre", width=150)
tabla_productos.column("precio", width=100)
tabla_productos.column("cantidad", width=100)
tabla_productos.column("categoria", width=150)

tabla_productos.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
#pantalla ingresar

pantalla_ingresar_productos = tk.Frame(ventana, bg="#20252d")

texto_ingresar = tk.Label(
    pantalla_ingresar_productos,
    text= "ingresar productos",
    font=("Arial", 12),
    bg="#20252d",
    fg="white",
    width= 22,
    height=2,
)
texto_ingresar.grid(row=0, column=0, columnspan=2, pady=20)

#pantalla eliminar productos
pantalla_eliminar = tk.Frame(ventana, bg="#20252d")


texto_eliminar = tk.Label(
    pantalla_eliminar,
    text= "eliminar producto",
    font=("Arial", 12),
    bg="#20252d",
    fg="White",
    width=22,
    height=2,
)
texto_eliminar.grid(row=0, column=0, columnspan= 2, pady= 20 )

#-----------------BOTONES-----------------

boton_ingresar_productos = tk.Button(
    pantalla_menu,
    text="Ingresar Producto",
    font=("Arial", 12),
    bg="#2563eb",
    fg="white",
    width= 22,
    height=2,
    cursor="hand2",
    command=ingresar_producto
)
boton_ingresar_productos.grid(row=4, column=3, padx=20)

boton_ingresar = tk.Button(
    pantalla_inicio,
    text="Ingresar al sistema",
    font=("Arial", 12),
    bg="#2563eb",
    fg="white",
    width= 22,
    height=2,
    cursor="hand2",
    command=mostrar_menu
)
boton_ingresar.grid(row=1, column=0, padx=20)


boton_volver = tk.Button(
    pantalla_menu,
    text="Volver al inicio",
    font=("Arial" ,12),
    bg="#2563eb",
    fg="white",
    width=22,
    height=2,
    cursor="hand2",
    command=volver_inicio
)
boton_volver.grid(row=1, column=3, padx=20)

boton_consulta = tk.Button(
    pantalla_menu,
    text="consultar producto",
    font=("Arial", 12),
    bg="#2563eb",
    fg="white",
    width= 22,
    height=2,
    cursor="hand2",
    command=consultar_producto
)
boton_consulta.grid(row=3, column=3, padx=20)

boton_salir = tk.Button(
    pantalla_menu,
    text= "Salir del programa",
    font=("Arial", 12),
    bg="#eb2525",
    fg="white",
    width= 22,
    height=2,
    cursor="hand2",
    command= salir_programa
)
boton_salir.grid(row=6, column=3, padx=20)

boton_volver_menu = tk.Button(
    pantalla_consulta,
    text="volver",
    cursor="hand2",
    command=lambda:volver_menu(pantalla_consulta)
)
boton_volver_menu.grid(row=7, column=4, padx=20)

boton_mostrar = tk.Button(
    pantalla_ingresar_productos,
    text="Ingresas producto",
    command=mostrar_info
)

boton_mostrar.grid(row=5, column=0, columnspan=2, pady=10)

boton_eliminar = tk.Button(
    pantalla_eliminar,
    text="Eliminar",
    command=eliminar_producto_tk
)
boton_eliminar.grid(row=3, column=0, padx=20)

boton_borrar = tk.Button(
    pantalla_menu,
    text="Borrar producto",
    font=("Arial", 12),
    bg="#2563eb",
    fg="white",
    width= 22,
    height=2,
    cursor="hand2",
    command=borrar_producto
)
boton_borrar.grid(row=5, column=3, padx= 10)

tk.Button(
    pantalla_ingresar_productos,
    text="Volver",
    cursor="hand2",
    command=lambda: volver_menu(pantalla_ingresar_productos)
).grid(row=7, column=0, columnspan=2)

tk.Button(
    pantalla_eliminar,
    text="Volver",
    cursor="hand2",
    command=lambda: volver_menu(pantalla_eliminar)
).grid(row=7, column=0, columnspan=2)

#eliminar producto
tk.Label(pantalla_eliminar, text= "ID del producto:", bg="#20252d", fg="white").grid(row=1, column=0, pady=10)
entrada_eliminar = tk.Entry(pantalla_eliminar)
entrada_eliminar.grid(row=2, column=1)

# Nombre
tk.Label(pantalla_ingresar_productos, text="Nombre:", bg="#20252d", fg="white").grid(row=1, column=0, pady=10)

entrada_nombre = tk.Entry(pantalla_ingresar_productos)
entrada_nombre.grid(row=1, column=1)

# Precio
tk.Label(pantalla_ingresar_productos, text="Precio:", bg="#20252d", fg="white").grid(row=2, column=0, pady=10)

entrada_precio = tk.Entry(pantalla_ingresar_productos)
entrada_precio.grid(row=2, column=1)

# Cantidad
tk.Label(pantalla_ingresar_productos, text="Cantidad:", bg="#20252d", fg="white").grid(row=3, column=0, pady=10)

entrada_cantidad = tk.Entry(pantalla_ingresar_productos)
entrada_cantidad.grid(row=3, column=1)

# Categoría
tk.Label(pantalla_ingresar_productos, text="Categoría:", bg="#20252d", fg="white").grid(row=4, column=0, pady=10)

entrada_categoria = ttk.Combobox(
    pantalla_ingresar_productos,
    values=["Bebidas", "Alimentos", "Electrónica", "Limpieza"]
)

entrada_categoria.grid(row=4, column=1)
entrada_categoria.config(state="readonly")

resultado = tk.Label(
    pantalla_ingresar_productos,
    text="Acá aparecerá la información",
    bg="#20252d",
    fg="white"
)

resultado.grid(row=6, column=0, columnspan=2, pady=20)

# Mostrar inicialmente la primera pantalla
pantalla_inicio.pack()

ventana.mainloop()
