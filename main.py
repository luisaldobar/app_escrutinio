from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import requests

app = Flask(__name__)
cors = CORS(app)

from Controladores.ControladorUsuario import ControladorUsuario
miControladorUsuario=ControladorUsuario()
from Controladores.ControladorMesa import ControladorMesa
miControladorMesa=ControladorMesa()
from Controladores.ControladorCandidato import ControladorCandidato
miControladorCandidato=ControladorCandidato()
from Controladores.ControladorPartido import ControladorPartido
miControladorPartido=ControladorPartido()
from Controladores.ControladorPermiso import ControladorPermiso
miControladorPermiso=ControladorPermiso()
from Controladores.ControladorPermisoRol import ControladorPermisoRol
miControladorPermisoRol=ControladorPermisoRol()
from Controladores.ControladorResultado import ControladorResultado
miControladorResultado=ControladorResultado()
from Controladores.ControladorRol import ControladorRol
miControladorRol=ControladorRol()

@app.route("/",methods=['GET'])
def test():
   json = {}
   json["message"]="Server running ..."
   return jsonify(json)

#=========  Servicio Usuario  ===============

@app.route("/usuarios",methods=['GET'])
def getUsuarios():
    json=miControladorUsuario.index()
    return jsonify(json)

@app.route("/usuarios",methods=['POST'])
def crearUsuario():
    data = request.get_json()
    json=miControladorUsuario.create(data)
    return jsonify(json)
@app.route("/usuarios/<string:id>",methods=['GET'])
def getUsuario(id):
    json=miControladorUsuario.show(id)
    return jsonify(json)
@app.route("/usuarios/<string:id>",methods=['PUT'])
def modificarUsuario(id):
    data = request.get_json()
    json=miControladorUsuario.update(id, data)
    return jsonify(json)

@app.route("/usuarios/<string:id>",methods=['DELETE'])
def eliminarUsuario(id):
    json=miControladorUsuario.delete(id)
    return jsonify(json)
#========= Servicios Mesa ==========
@app.route("/mesas",methods=['GET'])
def getMesas():
    json=miControladorMesa.index()
    return jsonify(json)

@app.route("/mesas",methods=['POST'])
def crearMesa():
    data = request.get_json()
    json=miControladorMesa.create(data)
    return jsonify(json)

@app.route("/mesas/<string:id>",methods=['GET'])
def getMesa(id):
    json=miControladorMesa.show(id)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json=miControladorMesa.update(id, data)
    return jsonify(json)

@app.route("/mesas/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    json=miControladorUsuario.delete(id)
    return jsonify(json)

#=========  Servicio Candidato  ===============

@app.route("/candidatos",methods=['GET'])
def getCandidatos():
    json=miControladorCandidato.index()
    return jsonify(json)

@app.route("/candidatos",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json=miControladorCandidato.create(data)
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['GET'])
def getCandidato(id):
    json=miControladorCandidato.show(id)
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json=miControladorCandidato.update(id, data)
    return jsonify(json)

@app.route("/candidatos/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    json=miControladorCandidato.delete(id)
    return jsonify(json)

#========= Servicios Partido ==========

@app.route("/partidos",methods=['GET'])
def getPartidos():
    json=miControladorPartido.index()
    return jsonify(json)

@app.route("/partidos",methods=['POST'])
def crearPartido():
    data = request.get_json()
    json=miControladorPartido.create(data)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['GET'])
def getpartidos(id):
    json=miControladorPartido.show(id)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json=miControladorPartido.update(id, data)
    return jsonify(json)

@app.route("/partidos/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    json=miControladorPartido.delete(id)
    return jsonify(json)

#=========  Servicio Permiso  ===============
@app.route("/permisos",methods=['GET'])
def getPermisos():
    json=miControladorPermiso.index()
    return jsonify(json)

@app.route("/permisos",methods=['POST'])
def crearPermiso():
    data = request.get_json()
    json=miControladorPermiso.create(data)
    return jsonify(json)
@app.route("/permisos/<string:id>",methods=['GET'])
def getPermiso(id):
    json=miControladorPermiso.show(id)
    return jsonify(json)
@app.route("/permisos/<string:id>",methods=['PUT'])
def modificarPermiso(id):
    data = request.get_json()
    json=miControladorPermiso.update(id, data)
    return jsonify(json)

@app.route("/permisos/<string:id>",methods=['DELETE'])
def eliminarPermiso(id):
    json=miControladorPermiso.delete(id)
    return jsonify(json)

#=========  Servicio PermisoRol  ===============
@app.route("/PermisosRoles",methods=['GET'])
def getPermisosRoles():
    json=miControladorPermisoRol.index()
    return jsonify(json)

@app.route("/PermisosRoles",methods=['POST'])
def crearPermisosRoles():
    data = request.get_json()
    json=miControladorPermisoRol.create(data)
    return jsonify(json)
@app.route("/PermisosRoles/<string:id>",methods=['GET'])
def getPermisoRol(id):
    json=miControladorPermisoRol.show(id)
    return jsonify(json)
@app.route("/PermisosRoles/<string:id>",methods=['PUT'])
def modificarPermisoRol(id):
    data = request.get_json()
    json=miControladorPermisoRol.update(id, data)
    return jsonify(json)

@app.route("/PermisosRoles/<string:id>",methods=['DELETE'])
def eliminarPermisoRol(id):
    json=miControladorPermisoRol.delete(id)
    return jsonify(json)

#=========  Servicio Resultado  ===============

@app.route("/resultados",methods=['GET'])
def getResultados():
    json=miControladorResultado.index()
    return jsonify(json)

@app.route("/resultados",methods=['POST'])
def crearResultado():
    data = request.get_json()
    json=miControladorResultado.create(data)
    return jsonify(json)
@app.route("/resultados/<string:id>",methods=['GET'])
def getResultado(id):
    json=miControladorResultado.show(id)
    return jsonify(json)
@app.route("/resultados/<string:id>",methods=['PUT'])
def modificarResultado(id):
    data = request.get_json()
    json=miControladorResultado.update(id, data)
    return jsonify(json)

@app.route("/resultados/<string:id>",methods=['DELETE'])
def eliminarResultado(id):
    json=miControladorResultado.delete(id)
    return jsonify(json)

#=========  Servicio Roles  ===============

@app.route("/roles",methods=['GET'])
def getRoles():
    json=miControladorRol.index()
    return jsonify(json)

@app.route("/roles",methods=['POST'])
def crearRol():
    data = request.get_json()
    json=miControladorRol.create(data)
    return jsonify(json)
@app.route("/roles/<string:id>",methods=['GET'])
def getRol(id):
    json=miControladorRol.show(id)
    return jsonify(json)
@app.route("/roles/<string:id>",methods=['PUT'])
def modificarRol(id):
    data = request.get_json()
    json=miControladorRol.update(id, data)
    return jsonify(json)

@app.route("/roles/<string:id>",methods=['DELETE'])
def eliminarRol(id):
    json=miControladorRol.delete(id)
    return jsonify(json)
#=========  Fin Servicios  ===============
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
