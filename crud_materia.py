import crud_academico

db = crud_academico.crud()

class crud_materia:
    def consultar(self, buscar):
        try:
            return db.consultar("SELECT * FROM materia WHERE nombre like '%"+ buscar +"%'")
        except Exception as e:
            print(f"Error en consultar materia: {e}")
            return []
    
    def administrar(self, datos):
        try:
            sql = ""
            valores = ()
            
            if datos['accion']=="nuevo":
                sql = """
                    INSERT INTO materia (codigo, nombre, creditos, descripcion)
                    VALUES (%s, %s, %s, %s)
                """
                valores = (datos['codigo'], datos['nombre'], datos['creditos'], datos['descripcion'])
            elif datos['accion']=="modificar":
                sql = """
                    UPDATE materia SET codigo=%s, nombre=%s, creditos=%s, descripcion=%s
                    WHERE idMateria=%s
                """
                valores = (datos['codigo'], datos['nombre'], datos['creditos'], datos['descripcion'], datos['idMateria'])
            elif datos['accion']=="eliminar":
                sql = "DELETE FROM materia WHERE idMateria=%s"
                valores = (datos['idMateria'],)
            
            return db.ejecutar(sql, valores)
        except Exception as e:
            print(f"Error en administrar materia: {e}")
            return str(e)