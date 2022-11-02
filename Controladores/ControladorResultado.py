from Repositorios.RepositorioResultado import RepositorioResultado
from Modelos.Resultado import Resultado
class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
    def index(self):
        return self.repositorioResultado.findAll()
    def create(self,infoResultado):
        nuevoResultado=Resultado(infoResultado)
        return self.repositorioResultado.save(nuevoResultado)
    def show(self,id):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__
    def update(self,id,infoResultado):
        resultadoActual=Resultado(self.repositorioResultado.findById(id))
        resultadoActual.id = infoResultado["id"]
        resultadoActual.numero_mesa=infoResultado["numero_mesa"]
        resultadoActual.id_partido = infoResultado["id_partido"]
        return self.repositorioResultado.save(resultadoActual)
    def delete(self,id):
        return self.repositorioResultado.delete(id)