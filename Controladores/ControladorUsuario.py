from Modelos.Usuario import Usuario
class ControladorUsuario():
    def __init__(self):
         print("Creando ControladorUsuario")
    def index(self):
         print("Listar todos los usuarios")
         unUsuario = {
             "id": "10100654",
             "seudonimo": "ldominguez",
             "correo": "ldominguez@gmail.com",
             "contrasenia": "123"
         }
         return [unUsuario]
    def create(self, infoUsuario):
         print("Crear un usuario")
         elUsuario = Usuario(infoUsuario)
         return elUsuario.__dict__
    def show(self, id):
        print("Mostrando un usuario con id ", id)
        elUsuario = {
            "id": "10100654",
             "seudonimo": "ldominguez",
             "correo": "ldominguez@gmail.com",
             "contrasenia": "123"
        }
        return elUsuario
    def update(self, id, infoUsuario):
        print("Actualizando usuario con id ", id)
        elUsuario = Usuario(infoUsuario)
        return elUsuario.__dict__
    def delete(self, id):
        print("Eliminando usuario con id ", id)
        return {"deleted_count": 1}