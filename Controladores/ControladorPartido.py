from Modelos.Partido import Partido
class ControladorPartido():
    def __init__(self):
         print("Creando ControladorPartido")
    def index(self):
         print("Listar todos los partidos")
         unPartido = {
             "id": "A2020",
             "nombre": "porColombia",
             "lema": "paz y libertad"

         }
         return [unPartido]
    def create(self, infoPartido):
         print("Crear un partido")
         elPartido = Partido(infoPartido)
         return elPartido.__dict__
    def show(self, id):
        print("Mostrando un partido con id ", id)
        elPartido = {
            "id": "A2020",
             "nombre": "porColombia",
             "lema": "paz y libertad"
        }
        return elPartido
    def update(self, id, infoPartido):
        print("Actualizando partido con id ", id)
        elPartido = Partido(infoPartido)
        return elPartido.__dict__
    def delete(self, id):
        print("Eliminando partido con id ", id)
        return {"deleted_count": 1}