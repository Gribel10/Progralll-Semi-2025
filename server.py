from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib import parse
from urllib.parse import urlparse, parse_qs
import json 
import crud_alumno
import crud_docente
import crud_materia
import crud_usuario

port = 3000

crudAlumno = crud_alumno.crud_alumno()
crudDocente = crud_docente.crud_docente()
crudMateria = crud_materia.crud_materia()
crudUsuario = crud_usuario.crud_usuario()

class miServidor(SimpleHTTPRequestHandler):
    def do_GET(self):
        url_parseada = urlparse(self.path)
        path = url_parseada.path
        parametros = parse_qs(url_parseada.query)

        if self.path=="/":
            self.path="login.html"
            return SimpleHTTPRequestHandler.do_GET(self)
        if self.path=="/index.html":
            self.path="index.html"
            return SimpleHTTPRequestHandler.do_GET(self)
        if self.path=="/alumnos":
            alumnos = crudAlumno.consultar("")
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(alumnos).encode('utf-8'))
        if self.path=="/docentes":
            docentes = crudDocente.consultar("")
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(docentes).encode('utf-8'))
        if self.path=="/materias":
            materias = crudMateria.consultar("")
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(materias).encode('utf-8'))
        if self.path=="/usuarios":
            usuarios = crudUsuario.consultar("")
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(usuarios).encode('utf-8'))
        if path=="/vistas":
            self.path = '/modulos/'+ parametros['form'][0] +'.html'
            return SimpleHTTPRequestHandler.do_GET(self)
    
    def do_POST(self):
        try:
            longitud = int(self.headers['Content-Length'])
            datos = self.rfile.read(longitud)
            datos = datos.decode("utf-8")
            datos = parse.unquote(datos)
            datos = json.loads(datos)
            
            if self.path == "/alumnos":
                resp = {"msg": crudAlumno.administrar(datos)}
            elif self.path == "/docentes":
                resp = {"msg": crudDocente.administrar(datos)}
            elif self.path == "/materias":
                resp = {"msg": crudMateria.administrar(datos)}
            elif self.path == "/usuarios":
                resp = {"msg": crudUsuario.administrar(datos)}
            elif self.path == "/login":
                resp = crudUsuario.validar_login(datos['usuario'], datos['clave'])
            else:
                resp = {"msg": "Ruta no encontrada"}
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(resp).encode("utf-8"))
        except Exception as e:
            print(f"Error en POST: {e}")
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_resp = {"msg": f"Error del servidor: {str(e)}"}
            self.wfile.write(json.dumps(error_resp).encode("utf-8"))

print("Servidor ejecutandose en el puerto", port)
server = HTTPServer(("localhost", port), miServidor)
server.serve_forever()