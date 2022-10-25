from Modelos.Candidato import Candidato
class ControladorCandidato():
    def __init__(self):
         print("Creando ControladorCandidato")
    def index(self):
         print("Listar todos los candidatos")
         unCandidato = {
             "cedula": "10100100",
             "numero_resolucion": "250 de 2022",
             "nombre": "Guillermo",
             "apellido": "Guerra"

         }
         return [unCandidato]
    def create(self, infoCandidato):
         print("Crear un candidato")
         elCandidato = Candidato(infoCandidato)
         return elCandidato.__dict__
    def show(self, cedula):
        print("Mostrando un candidato con cedula ", id)
        elCandidato = {
            "cedula": "10100100",
             "numero_resolucion": "250 de 2022",
             "nombre": "Guillermo",
             "apellido": "Guerra"
        }
        return elCandidato
    def update(self, id, infoCandidato):
        print("Actualizando candidato con id ", id)
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__
    def delete(self, id):
        print("Eliminando candidato con id ", id)
        return {"deleted_count": 1}