import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from Clientes import *
from Conexion import *
from Productos import *

class formularioClientes:

    global base
    base=None
    global textBoxId
    textBoxId= None
    global textBoxNombres
    textBoxNombre=None
    global textBoxApellidos
    textBoxApellidos=None
    global combo
    combo=None
    global groupBox
    groupBox=None
    global tree
    tree=None
    global textBoxIdUsuario
    textBoxIdUsuario=None
    global textBoxNombreProducto
    textBoxNombreProducto=None
    global textBoxCantidad
    textBoxCantidad=None
    global textBoxPrecio
    textBoxPrecio=None

def formulario():
        global textBoxId,textBoxNombres,textBoxApellidos,combo,groupBox,tree,base
        try:
            base= Tk()
            base.geometry("1200x500")
            base.title("Formulario Python")
            
            groupBox = LabelFrame(base,text="Datos del Personal",padx=5,pady=5)
            groupBox.grid(row=0,column=0,padx=10,pady=10)
            
            labelId=Label(groupBox,text="Id:",width=13,font=("arial",12)).grid(row=0,column=0)
            textBoxId=Entry(groupBox)
            textBoxId.grid(row=0,column=1)

            labelNombres=Label(groupBox,text="Nombres:",width=13,font=("arial",12)).grid(row=1,column=0)
            textBoxNombres=Entry(groupBox)
            textBoxNombres.grid(row=1,column=1)
            
            labelApellidos=Label(groupBox,text="Apellidos:",width=13,font=("arial",12)).grid(row=2,column=0)
            textBoxApellidos=Entry(groupBox)
            textBoxApellidos.grid(row=2,column=1)

            labelSexo=Label(groupBox,text="Sexo:",width=13,font=("arial",12)).grid(row=3,column=0)
            selecionSexo=tk.StringVar()
            combo= ttk.Combobox(groupBox,values=["Masculino","Femenino"],textvariable=selecionSexo)
            combo.grid(row=3,column=1)
            selecionSexo.set("Masculino")

            Button(groupBox,text="Guardar",width=10,command=guardaRegistros).grid(row=4,column=0)
            Button(groupBox,text="Modificar",width=10,command=modificarRegistros).grid(row=4,column=1)
            Button(groupBox,text="Eliminar",width=10,command=eliminarRegistros).grid(row=4,column=2)

            groupBox=LabelFrame(base,text="Lista del Personal",padx=5,pady=5)
            groupBox.grid(row=0,column=1,padx=5,pady=5)
            
            tree =ttk.Treeview(groupBox,columns=("Id","Nombre","Apellido","Sexo"),show='headings',height=5)
            tree.grid(row=5, column=0, columnspan=3)
            tree.column("# 1",anchor=CENTER)
            tree.heading("#1",text="Id")
            tree.column("# 2",anchor=CENTER)
            tree.heading("#2",text="Nombre")
            tree.column("# 3",anchor=CENTER)
            tree.heading("#3",text="Apellido")
            tree.column("# 4",anchor=CENTER)
            tree.heading("#4",text="Sexo")
            
            for row in CClientes.mostrarClientes():
                tree.insert("","end",values=row)
                
            tree.bind("<<TreeviewSelect>>",selecionarRegistro)
            actualizartreeView()
            formularioProductos()
            tree.pack()
            base.mainloop()
        except ValueError as error:
            print("Error al montrar la interfaz, error: {}".format(error))

def guardaRegistros():
        global textBoxNombres,textBoxApellidos,combo,groupBox
        try:
            if textBoxNombres is None or textBoxApellidos is None or combo is None:
                print("Los widgets no estan inicializados")
                return
            nombres=textBoxNombres.get()
            apellidos=textBoxApellidos.get()
            sexo=combo.get()
            CClientes.ingresarClientes(nombres,apellidos,sexo)
            messagebox.showinfo("Informacion","Los datos fueron guardados")
            actualizartreeView()
            
            textBoxNombres.delete(0,END)
            textBoxApellidos.delete(0,END)
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))

def actualizartreeView():
    global tree
    try:
        tree.delete(*tree.get_children())
        datos=CClientes.mostrarClientes()
        for row in CClientes.mostrarClientes():
            tree.insert("","end",values=row)
    except ValueError as error:
        print("Error al actualizar tabla {}".format(error))

def selecionarRegistro(event):
    try:
        itemSelecion= tree.focus()
        if itemSelecion:
            values=tree.item(itemSelecion)['values']
            
            textBoxId.delete(0,END)
            textBoxId.insert(0,values[0])
            textBoxNombres.delete(0,END)
            textBoxNombres.insert(0,values[1])
            textBoxApellidos.delete(0,END)
            textBoxApellidos.insert(0,values[2])
            combo.set(values[3])
    except ValueError as error:
        print("Error al seleccionar registro {}".format(error))

def modificarRegistros():
        global textBoxId,textBoxNombres,textBoxApellidos,combo
        try:
            if textBoxId is None or textBoxNombres is None or textBoxApellidos is None or combo is None:
                print("Los widgets no estan inicializados")
                return            
            idUsuario=textBoxId.get()
            nombres=textBoxNombres.get()
            apellidos=textBoxApellidos.get()
            sexo=combo.get()
            CClientes.modificarClientes(idUsuario,nombres,apellidos,sexo)
            messagebox.showinfo("Informacion","Los datos fueron actualizados")
            actualizartreeView()
            
            textBoxId.delete(0,END)
            textBoxNombres.delete(0,END)
            textBoxApellidos.delete(0,END)
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))

def eliminarRegistros():
        global textBoxId,textBoxNombres,textBoxApellidos
        try:
            if textBoxId is None:
                print("Los widgets no estan inicializados")
                return
            
            idUsuario=textBoxId.get()
            CClientes.EliminarClientes(idUsuario)
            messagebox.showinfo("Informacion","Los datos fueron eliminados")
            
            actualizartreeView()

            textBoxId.delete(0,END)
            textBoxNombres.delete(0,END)
            textBoxApellidos.delete(0,END)
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))
def formularioProductos():
    global base, treeProductos, textBoxIdUsuario, textBoxNombreProducto,textBoxCantidad,textBoxPrecio
    groupBoxProductos = LabelFrame(base, text="Gestión de Productos", padx=5, pady=5)
    groupBoxProductos.grid(row=1, column=0, padx=10, pady=10, columnspan=5)  # Ubicación

    Label(groupBoxProductos, text="ID Usuario:", width=13).grid(row=0, column=0, padx=5, pady=5)
    textBoxIdUsuario = Entry(groupBoxProductos)
    textBoxIdUsuario.grid(row=0, column=1, padx=5, pady=5)

    Label(groupBoxProductos, text="Nombre Producto:", width=13).grid(row=1, column=0, padx=5, pady=5)
    textBoxNombreProducto = Entry(groupBoxProductos)
    textBoxNombreProducto.grid(row=1, column=1, padx=5, pady=5)

    Label(groupBoxProductos, text="Cantidad:", width=13).grid(row=2, column=0, padx=5, pady=5)
    textBoxCantidad = Entry(groupBoxProductos)
    textBoxCantidad.grid(row=2, column=1, padx=5, pady=5)

    Label(groupBoxProductos, text="Precio:", width=13).grid(row=3, column=0, padx=5, pady=5)
    textBoxPrecio = Entry(groupBoxProductos)
    textBoxPrecio.grid(row=3, column=1, padx=5, pady=5)
    
    Button(groupBoxProductos, text="Guardar", width=10, command=lambda: guardaProducto(textBoxIdUsuario, textBoxNombreProducto, textBoxCantidad, textBoxPrecio)).grid(row=4, column=0, padx=5, pady=5)
    Button(groupBoxProductos, text="Modificar", width=10, command=modificarProducto).grid(row=4, column=1, padx=5, pady=5)
    Button(groupBoxProductos, text="Eliminar", width=10, command=eliminarProducto).grid(row=4, column=2, padx=5, pady=5)

    treeProductos = ttk.Treeview(groupBoxProductos, columns=("Id", "ID Usuario", "Nombre", "Cantidad", "Precio"), show='headings', height=5)
    treeProductos.grid(row=5, column=0, columnspan=15, padx=5, pady=5)
    treeProductos.column("#1", anchor=CENTER)
    treeProductos.heading("#1", text="Id")
    treeProductos.column("#2", anchor=CENTER)
    treeProductos.heading("#2", text="ID Usuario")
    treeProductos.column("#3", anchor=CENTER)
    treeProductos.heading("#3", text="Nombre")
    treeProductos.column("#4", anchor=CENTER)
    treeProductos.heading("#4", text="Cantidad")
    treeProductos.column("#5", anchor=CENTER)
    treeProductos.heading("#5", text="Precio")

    treeProductos.bind("<<TreeviewSelect>>", selecionarRegistroProducto)
    actualizarTreeProductos()

def guardaProducto(id_usuario, nombre_producto, cantidad, precio):
    try:
        id_usuario = id_usuario.get()
        nombre_producto = nombre_producto.get()
        cantidad = int(cantidad.get())
        precio = float(precio.get())
        CProductos.ingresarProducto(id_usuario, nombre_producto, cantidad, precio)
        messagebox.showinfo("Información", "Producto guardado exitosamente")
        actualizarTreeProductos()
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar producto: {e}")

def actualizarTreeProductos():
    for row in treeProductos.get_children():
        treeProductos.delete(row)
    for producto in CProductos.mostrarProductos():
        treeProductos.insert("", "end", values=producto)

def modificarProducto():
    global treeProductos,textBoxIdUsuario,textBoxNombreProducto,textBoxCantidad,textBoxPrecio
    try:
        itemSelecion = treeProductos.focus()
        if not itemSelecion:
            messagebox.showwarning("Advertencia", "Por favor selecciona un producto para modificar.")
            return
        valores = treeProductos.item(itemSelecion, 'values')
        id_producto = valores[0]
        id_usuario = textBoxIdUsuario.get()
        nombre_producto = textBoxNombreProducto.get()
        cantidad = int(textBoxCantidad.get())
        precio = float(textBoxPrecio.get())
        
        CProductos.modificarProducto(id_producto, id_usuario, nombre_producto, cantidad, precio)
        messagebox.showinfo("Información", "Producto actualizado exitosamente.")
        
        actualizarTreeProductos()
        limpiarCamposProductos()
    except Exception as e:
        messagebox.showerror("Error", f"Error al modificar el producto: {e}")

def eliminarProducto():
    global treeProductos
    try:
        itemSelecion = treeProductos.focus()
        if not itemSelecion:
            messagebox.showwarning("Advertencia", "Por favor selecciona un producto para eliminar.")
            return
        valores = treeProductos.item(itemSelecion, 'values')
        id_producto = valores[0]
        respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas eliminar este producto?")
        if respuesta:
            CProductos.eliminarProducto(id_producto)
            messagebox.showinfo("Información", "Producto eliminado exitosamente.")
            actualizarTreeProductos()
    except Exception as e:
        messagebox.showerror("Error", f"Error al eliminar el producto: {e}")

def selecionarRegistroProducto(event):
    try:
        itemSelecion = treeProductos.focus()
        if itemSelecion:
            values = treeProductos.item(itemSelecion)['values']
            textBoxIdUsuario.delete(0, END)
            textBoxIdUsuario.insert(0, values[1])
            textBoxNombreProducto.delete(0, END)
            textBoxNombreProducto.insert(0, values[2])
            textBoxCantidad.delete(0, END)
            textBoxCantidad.insert(0, values[3])
            textBoxPrecio.delete(0, END)
            textBoxPrecio.insert(0, values[4])
    except ValueError as error:
        print("Error al seleccionar registro de producto: {}".format(error))

def limpiarCamposProductos():
    try:
        textBoxIdUsuario.delete(0, END)
        textBoxNombreProducto.delete(0, END)
        textBoxCantidad.delete(0, END)
        textBoxPrecio.delete(0, END)
    except Exception as e:
        print("Error al limpiar los campos de productos: {}".format(e))

formulario()
