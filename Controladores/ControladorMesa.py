from Modelos.Mesa import Mesa
class ControladorMesa():
    def __init__(self):
         print("Creando ControladorMesa")
    def index(self):
         print("Listar todas las mesas")
         unaMesa = {
             "numero": "700",
             "cantidad_inscritos": "250"
         }

         return [unaMesa]
    def create(self, infoMesa):
         print("Crear una mesa")
         laMesa = Mesa(infoMesa)
         return laMesa.__dict__


    def show(self, numero):
        print("Mostrando una mesa con su número ", numero)
        laMesa = {
            "numero": "700",
             "cantidad_inscritos": "250"
        }
        return laMesa
    def update(self, numero, infoMesa):
        print("Actualizando mesa por numero ", numero)
        laMesa = Mesa(infoMesa)
        return laMesa.__dict__

    def delete(self, numero):
        print("Eliminando mesa por número ", numero)
        return {"deleted_count": 1}