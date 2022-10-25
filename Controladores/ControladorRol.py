from Modelos.Rol import Rol
class ControladorRol():
    def __init__(self):
         print("Creando ControladorRol")
    def index(self):
         print("Listar todos los Roles")
         unRol = {
             "id": "01",
             "nombre": "administrador"

         }
         return [unRol]
    def create(self, infoRol):
         print("Crear un Rol")
         elRol = Rol(infoRol)
         return elRol.__dict__
    def show(self, id):
        print("Mostrando un rol con id ", id)
        elRol = {
            "id": "01",
             "nombre": "administrador"

        }
        return elRol
    def update(self, id, infoRol):
        print("Actualizando rol con id ", id)
        elRol = Rol(infoRol)
        return elRol.__dict__
    def delete(self, id):
        print("Eliminando rol con id ", id)
        return {"deleted_count": 1}