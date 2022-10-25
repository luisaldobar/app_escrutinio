from Modelos.Resultado import Resultado
class ControladorResultado():
    def __init__(self):
         print("Creando ControladorResultado")
    def index(self):
         print("Listar todos los resultados")
         unResultado = {
             "id": "R100",
             "numero_mesa": "700",
             "id_partido": "A2020"
         }
         return [unResultado]
    def create(self, infoResultado):
         print("Crear un resultado")
         elResultado = Resultado(infoResultado)
         return elResultado.__dict__
    def show(self, id):
        print("Mostrando un resultado con id ", id)
        elResultado = {
             "id": "R100",
             "numero_mesa": "700",
             "id_partido": "A2020"

        }
        return elResultado
    def update(self, id, infoResultado):
        print("Actualizando resultado con id ", id)
        elResultado = Resultado(infoResultado)
        return elResultado.__dict__
    def delete(self, id):
        print("Eliminando resultado con id ", id)
        return {"deleted_count": 1}