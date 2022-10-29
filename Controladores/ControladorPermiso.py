from Modelos.Permiso import Permiso
class ControladorPermiso():
    def __init__(self):
         print("Creando ControladorPermiso")
    def index(self):
         print("Listar todos los permisos")
         unPermiso = {
             "id": 10,
             "url": "http://127.0.0.1:8080",
             "metodo": "Get"

         }
         return [unPermiso]
    def create(self, infoPermiso):
         print("Crear un permiso")
         elPermiso = Permiso(infoPermiso)
         return elPermiso.__dict__
    def show(self, id):
        print("Mostrando un permiso con id ", id)
        elPermiso = {
            "id": 10,
             "url": "http://127.0.0.1:8080",
             "metodo": "Get"
        }
        return elPermiso
    def update(self, id, infoPermiso):
        print("Actualizando permiso con id ", id)
        elPermiso = Permiso(infoPermiso)
        return elPermiso.__dict__
    def delete(self, id):
        print("Eliminando permiso con id ", id)
        return {"deleted_count": 1}