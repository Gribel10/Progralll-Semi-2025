import crud_academico

db = crud_academico.crud()

class crud_docente:
    def consultar(self, buscar):
        try:
            return db.consultar("SELECT * FROM docente WHERE nombre like '%"+ buscar +"%'")
        except Exception as e:
            print(f"Error en consultar docente: {e}")
            return []
    
    def administrar(self, datos):
        try:
            sql = ""
            valores = ()
            
            if datos['accion']=="nuevo":
                sql = """
                    INSERT INTO docente (codigo, nombre, direccion, telefono, email)
                    VALUES (%s, %s, %s, %s, %s)
                """
                valores = (datos['codigo'], datos['nombre'], datos['direccion'], datos['telefono'], datos['email'])
            elif datos['accion']=="modificar":
                sql = """
                    UPDATE docente SET codigo=%s, nombre=%s, direccion=%s, telefono=%s, email=%s
                    WHERE idDocente=%s
                """
                valores = (datos['codigo'], datos['nombre'], datos['direccion'], datos['telefono'], datos['email'], datos['idDocente'])
            elif datos['accion']=="eliminar":
                sql = "DELETE FROM docente WHERE idDocente=%s"
                valores = (datos['idDocente'],)
            
            return db.ejecutar(sql, valores)
        except Exception as e:
            print(f"Error en administrar docente: {e}")
            return str(e)