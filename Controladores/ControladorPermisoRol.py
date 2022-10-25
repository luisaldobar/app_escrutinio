from Modelos.PermisoRol import PermisoRol
class ControladorPermisoRol():
    def __init__(self):
         print("Creando ControladorPermisoRol")
    def index(self):
         print("Listar todos los PermisoRol")
         unPermisoRol = {
             "id": "20",
             "id_rol": "01",
             "id_permiso": "10"

         }
         return [unPermisoRol]
    def create(self, infoPermisoRol):
         print("Crear un PermisoRol")
         elPermisoRol = PermisoRol(infoPermisoRol)
         return elPermisoRol.__dict__
    def show(self, id):
        print("Mostrando un PermisoRol con id ", id)
        elPermisoRol = {
            "id": "20",
             "id_rol": "01",
             "id_permiso": "10"
        }
        return elPermisoRol
    def update(self, id, infoPermisoRol):
        print("Actualizando PermisoRol con id ", id)
        elPermisoRol = PermisoRol(infoPermisoRol)
        return elPermisoRol.__dict__
    def delete(self, id):
        print("Eliminando PermisoRol con id ", id)
        return {"deleted_count": 1}