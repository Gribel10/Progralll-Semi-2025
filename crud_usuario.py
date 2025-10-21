import crud_academico

db = crud_academico.crud()

class crud_usuario:
    def consultar(self, buscar):
        try:
            return db.consultar("SELECT * FROM usuarios WHERE nombre like '%"+ buscar +"%' OR usuario like '%"+ buscar +"%'")
        except Exception as e:
            print(f"Error en consultar usuario: {e}")
            return []
    
    def administrar(self, datos):
        try:
            sql = ""
            valores = ()
            
            if datos['accion']=="nuevo":
                sql = """
                    INSERT INTO usuarios (usuario, clave, nombre, direccion, telefono)
                    VALUES (%s, %s, %s, %s, %s)
                """
                valores = (datos['usuario'], datos['clave'], datos['nombre'], datos['direccion'], datos['telefono'])
            elif datos['accion']=="modificar":
                sql = """
                    UPDATE usuarios SET usuario=%s, clave=%s, nombre=%s, direccion=%s, telefono=%s
                    WHERE idUsuario=%s
                """
                valores = (datos['usuario'], datos['clave'], datos['nombre'], datos['direccion'], datos['telefono'], datos['idUsuario'])
            elif datos['accion']=="eliminar":
                sql = "DELETE FROM usuarios WHERE idUsuario=%s"
                valores = (datos['idUsuario'],)
            
            return db.ejecutar(sql, valores)
        except Exception as e:
            print(f"Error en administrar usuario: {e}")
            return str(e)
    
    def validar_login(self, usuario, clave):
        try:
            resultado = db.consultar(f"SELECT * FROM usuarios WHERE usuario='{usuario}' AND clave='{clave}'")
            if resultado and len(resultado) > 0:
                return {"valido": True, "usuario": resultado[0]}
            return {"valido": False}
        except Exception as e:
            print(f"Error en validar_login: {e}")
            return {"valido": False, "error": str(e)}