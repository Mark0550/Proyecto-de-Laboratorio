from Conexion import *

class CProductos:

    @staticmethod
    def mostrarProductos():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("SELECT * FROM productos;")
            resultado = cursor.fetchall()
            cone.close()
            return resultado
        except mysql.connector.Error as error:
            print("Error al mostrar productos: {}".format(error))

    @staticmethod
    def ingresarProducto(id_usuario, nombre_producto, cantidad, precio):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "INSERT INTO productos (id_usuario, nombre_producto, cantidad, precio) VALUES (%s, %s, %s, %s);"
            valores = (id_usuario, nombre_producto, cantidad, precio)
            cursor.execute(sql, valores)
            cone.commit()
            cone.close()
            print(cursor.rowcount, "Producto(s) ingresado(s)")
        except mysql.connector.Error as error:
            print("Error al ingresar producto: {}".format(error))

    @staticmethod
    def modificarProducto(id, id_usuario, nombre_producto, cantidad, precio):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "UPDATE productos SET id_usuario = %s, nombre_producto = %s, cantidad = %s, precio = %s WHERE id = %s;"
            valores = (id_usuario, nombre_producto, cantidad, precio, id)
            cursor.execute(sql, valores)
            cone.commit()
            cone.close()
            print(cursor.rowcount, "Producto(s) actualizado(s)")
        except mysql.connector.Error as error:
            print("Error al modificar producto: {}".format(error))

    @staticmethod
    def eliminarProducto(id):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "DELETE FROM productos WHERE id = %s;"
            cursor.execute(sql, (id,))
            cone.commit()
            cone.close()
            print(cursor.rowcount, "Producto(s) eliminado(s)")
        except mysql.connector.Error as error:
            print("Error al eliminar producto: {}".format(error))