from Conexion import *

class CClientes:

    def mostrarClientes():
        try:
            cone=CConexion.ConexionBaseDeDatos()
            cursor=cone.cursor()
            cursor.execute("select * from usuarios;")
            miResultado=cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado
        except mysql.connector.Error as error:
            print("Error de mostrar datos {}".format(error))

    def ingresarClientes(nombres,apellido,sexo):
        
        try:
            cone=CConexion.ConexionBaseDeDatos()
            cursor=cone.cursor()
            sql="insert into usuarios values(null,%s,%s,%s);"
            # La variable valores tiene que ser una tupla
            # Como minimo expresion es: (valor,) la coma hace que sea una tupla
            # Las tuplas son listas inmutables, eso quiere decir que no se pueden modificar
            valores=(nombres,apellido,sexo)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registros Ingresado")
            cone.close()
        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))
            
    def modificarClientes(idUsuario,nombres,apellido,sexo):
        
        try:
            cone=CConexion.ConexionBaseDeDatos()
            cursor=cone.cursor()
            sql="update usuarios set usuarios.nombres=%s,usuarios.apellidos=%s,usuarios.sexo=%s where usuarios.id=%s;"
            valores=(nombres,apellido,sexo,idUsuario)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registros Actualizado")
            cone.close()
        except mysql.connector.Error as error:
            print("Error de actualizacion de datos {}".format(error))
    
    def EliminarClientes(idUsuario):
        
        try:
            cone=CConexion.ConexionBaseDeDatos()
            cursor=cone.cursor()
            sql="delete from usuarios where usuarios.id=%s;"
            valores=(idUsuario,)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registros Eliminado")
            cone.close()
        except mysql.connector.Error as error:
            print("Error de eliminacion de datos {}".format(error))