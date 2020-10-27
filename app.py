from flask import Flask, request, jsonify
from Usuarios import Usuarios
from CRUD_Usuarios import CRUD_Usuarios
from CRUD_Videojuegos import CRUD_Videojuegos
from flask_cors import CORS
import json



lista_usuarios = CRUD_Usuarios()
lista_videojuegos = CRUD_Videojuegos()

#CREACIÓN DEL ADMINISTRADOR
lista_usuarios.agregar_usuario("Usuario", "Maestro", "admin", "admin")


app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['POST'])
def login():

	if request.method == 'POST':

		user = request.json['usuario']
		passw = request.json['password']

		usuario = lista_usuarios.validar_usuario(user,passw)

		if usuario is not False:

			respuesta = {

            	'id': usuario.id, 
            	'nombre': usuario.nombre,
            	'apellido': usuario.apellido,
            	'usuario': usuario.usuario,
           		'estado': 1
            }

			return respuesta

		return jsonify({

			'message':'No se encontró el Usuario',
			'estado': 0

			})
	

@app.route('/registro', methods=['POST'])
def registro():

	if request.method == 'POST':

		nombre = request.json['nombre']
		apellido = request.json['apellido']
		user = request.json['usuario']
		passw = request.json['password']

		usuario = lista_usuarios.agregar_usuario(nombre, apellido, user, passw)

		if usuario is not False:

			return jsonify({'message':'Se registro el usuario'})

		return jsonify({'message':'El Usuario ya existe'})



@app.route('/recuperacion-pass', methods=['POST'])
def recuperacion():	

	if request.method == 'POST':

		user = request.json['usuario']

		passw = lista_usuarios.recuperar_pass(user)

		if passw is not False:

			return jsonify({'message':'Su contraseña es:' + passw})

		return jsonify({'message':'No se encontró el Usuario'})	


@app.route('/', methods=['GET'])
def index():

	return "<H1>Bienvenido a mis dominios</H1>"

if __name__ == "__main__":
	app.run(threaded=True, port=5000,debug=True)		