from flask import Flask, request, jsonify
from Usuarios import Usuarios

listaUsuarios = []
contador = 1

#ADMINISTRADOR
listaUsuarios.append(Usuarios(0,"Usuario","Maestro","admin","admin"))

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():

	if request.method == 'POST':

		nombre = request.form.get('usuario')
		passw = request.form.get('pass')

		for user in listaUsuarios:

			if user.getUsuario() == nombre and user.getPassword() == passw:
				return user.dump()

		return "Usuario No Encontrado"		

@app.route('/registro', methods=['POST'])
def registro():

	if request.method == 'POST':

		nombre = request.form.get('Nombre')
		apellido = request.form.get('Apellido')
		usuario = request.form.get('Usuario')
		passw = request.form.get('Password')

		for user in listaUsuarios:

			contador_temporal = 0

			if user.getUsuario() == usuario:

				return "El Usuario ya Existe"

			elif contador_temporal == contador:

				listaUsuarios.append(Usuarios(contador, nombre, apellido, usuario, passw))
				contador += 1

				return user.dump()

			else:
				contador_temporal += 1

@app.route('/recuperacion-contraseña', methods=['POST'])
def recuperacion():	

	if request.method == 'POST':

		usuario = request.form.get('Usuario')

		for user in listaUsuarios:

			contador_temporal = 0

			if user.getUsuario() == usuario:

				return "El Usuario ya Existe"

			elif contador_temporal == contador:

				return user.dump()

			else:
				contador_temporal += 1

@app.route('/', methods=['GET'])
def index():

	return "<H1>Bienvenido a mis dominios</H1>"

if __name__ == "__main__":
	app.run(threaded=True, port=5000,debug=True)		