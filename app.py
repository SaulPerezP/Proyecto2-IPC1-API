from flask import Flask, request, jsonify
from Usuarios import Usuarios
from CRUD_Usuarios import CRUD_Usuarios
from CRUD_Videojuegos import CRUD_Videojuegos
from CRUD_Biblioteca import CRUD_Biblioteca
from CRUD_Comentarios import CRUD_Comentarios
from flask_cors import CORS
import json
import csv


lista_usuarios = CRUD_Usuarios()
lista_videojuegos = CRUD_Videojuegos()
lista_biblioteca = CRUD_Biblioteca()
lista_comentarios = CRUD_Comentarios()

#CREACIÓN DEL ADMINISTRADOR
lista_usuarios.agregar_usuario("Usuario", "Maestro", "admin", "admin", "administrador")

#CREACIÓN DE VIDEOJUEGOS
lista_videojuegos.agregar_videojuego("Need for Speed Rivals","2013","243.00","Carreras",
	"Automóviles","","https://images-na.ssl-images-amazon.com/images/I/81AgKYhBG6L._AC_SL1500_.jpg",
	"https://www.nextgenbase.com/files/2013/12/NFS-main-1.jpg",
	"En Need for Speed  Rivals Elige si prefieres jugar como policía o como corredor, ya que cada bando tendrá sus propios retos, apuestas, recompensas y consecuencias. Como corredor tu meta será alcanzar la fama corriendo riesgos y capturando en vídeo tus huidas más espectaculares para que todo el mundo vea de lo que eres capaz. Cuantos más policías evites, más Speedpoints conseguirás, desbloqueando nuevos coches y objetos.")

lista_videojuegos.agregar_videojuego("Fifa 21","2021","355.87","Deporte","Multijugador","Fútbol",
	"https://s2.gaming-cdn.com/images/products/7543/orig/fifa-21-xbox-one-cover.jpg",
	"https://www.eluniverso.com/sites/default/files/styles/nota_ampliada_normal_foto/public/fotos/2020/07/fifa-21.jpg?itok=CynaSUnL","FIFA 21 es un videojuego de simulación de fútbol del año 2020 disponible para Microsoft Windows, PlayStation 4, Xbox One y Nintendo Switch el 9 de octubre de 2020")

lista_videojuegos.agregar_videojuego("Minecraft","2009","233.84","Aventura","Supervivencia","",
	"https://images-na.ssl-images-amazon.com/images/I/7135wf8VGVL._SL1106_.jpg",
	"https://cdn02.nintendo-europe.com/media/images/10_share_images/games_15/nintendo_switch_4/H2x1_NSwitch_Minecraft_image1280w.jpg",
	"Minecraft es un videojuego de construcción, de tipo «mundo abierto» o sandbox creado originalmente por el sueco Markus Persson (conocido comúnmente como Notch), y posteriormente desarrollado por su empresa, Mojang Studios. Fue lanzado públicamente el 17 de mayo de 2009, después de diversos cambios fue lanzada su versión completa el 18 de noviembre de 2011.")

lista_videojuegos.agregar_videojuego("Rocket League","2015","311.89","Multijugador","Fútbol","Automóviles",
	"https://cdn.game.tv/game-tv-content/images_2/mobile/game_banner/dd1c118bd597b468a356e835ea9b8758/en/dd1c118bd597b468a356e835ea9b8758.jpg",
	"https://www.gamerswithjobs.com/files/styles/front_page_feature/public/images/forum/rocketbanner.jpg?itok=-qABVMJt",
	"Rocket League es un videojuego que combina el fútbol con los vehículos. Fue desarrollado por Psyonix y lanzado el 7 de julio del 2015. Se encuentra disponible en español, tiene modos de juego cooperativo, de un jugador y en línea")


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
            	'tipo': usuario.tipo,
           		'estado': 1
            }

			return respuesta

		return {

			'estado': 2

		}
	

@app.route('/registro', methods=['POST'])
def registro():

	if request.method == 'POST':

		nombre = request.json['nombre']
		apellido = request.json['apellido']
		user = request.json['usuario']
		passw = request.json['password']
		conf_passw = request.json['conf_password']
		tipo = request.json['tipo']


		#VALIDAR CONTRASEÑAS
		if passw == conf_passw:

			usuario = lista_usuarios.agregar_usuario(nombre, apellido, user, passw, tipo)

			#VALIDAR SI EL USUARIO ESTA DISPONIBLE | ESTADO 1: USUARIO DISPONIBLE
			if usuario is not False:

				return {

				'nombre': nombre,
				'apellido': apellido,
				'usuario': user,
				'tipo': tipo,
				'estado': 1

				}

			#ESTADO 2: USUARIO NO DISPONIBLE	
			return {

				'usuario': user,
				'estado': 2

			}	

		#ESTADO 3: LAS CONTRASEÑAS NO COINCIDEN	
		return {

			'estado': 3
		
		}	


@app.route('/recuperacion-pass', methods=['POST'])
def recuperacion():	

	if request.method == 'POST':

		user = request.json['usuario']

		usuario = lista_usuarios.recuperar_pass(user)

		if usuario is not False:

			return {

				'usuario': usuario.usuario,
				'pass': usuario.password,
				'tipo': usuario.tipo,
				'estado': 1
			}

		return {

			'usuario': 'Usuario no encontrado'
		}

@app.route('/creacion-juego', methods=['POST'])
def creacion_juego():

	if request.method == 'POST':

		nombre = request.json['nombre']
		anio = request.json['anio']
		precio = request.json['precio']
		cat1 = request.json['cat1']
		cat2 = request.json['cat2']
		cat3 = request.json['cat3']
		foto = request.json['foto']
		banner = request.json['banner']
		desc = request.json['descripcion']

		lista_videojuegos.agregar_videojuego(nombre,anio,precio,cat1,cat2,cat3,foto,banner,desc)
		lista_videojuegos.lista_categorias(cat1)
		lista_videojuegos.lista_categorias(cat2)
		lista_videojuegos.lista_categorias(cat3)

		return {

			'nombre': nombre,
			'anio': anio,
			'precio': precio,
			'categoria1': cat1,
			'categoria2': cat2,
			'categoria3': cat3,
			'foto': foto,
			'banner': banner,
			'estado': 1

		}

@app.route('/modificar-juego', methods=['POST'])
def modificar_juego():

	if request.method == 'POST':

		id = request.json['id']
		nombre = request.json['nombre']
		anio = request.json['anio']
		precio = request.json['precio']
		cat1 = request.json['cat1']
		cat2 = request.json['cat2']
		cat3 = request.json['cat3']
		foto = request.json['foto']
		banner = request.json['banner']
		desc = request.json['descripcion']

		respuesta = lista_videojuegos.modificar_videojuego(int(id),nombre,anio,precio,cat1,
			cat2,cat3,foto,banner,desc)

		if juego is not False:

			return {

			'data': respuesta,
			'estado': 1

			}

		return {
		
			'estado': 2
		}	


@app.route('/mostrar-juegos', methods=['GET'])
def mostrar_juego():

	if request.method == 'GET':

		return lista_videojuegos.mostrar_todos()

@app.route('/info-juego', methods=['GET'])
def info_juego():

	if request.method == 'GET':

		id = request.args.get("id",None)
		juego = lista_videojuegos.info_individual(int(id))

		if juego is not None:

			return{

				'id': id,
				'data': juego
			}

		return	{

			'estado': 2
		}

@app.route('/biblioteca', methods=['POST'])
def biblioteca():

	if request.method == 'POST':

		id_usuario = request.json['id_usuario']
		id_juego = request.json['id_juego']
		nombre_juego = request.json['nombre_juego']
		foto_juego = request.json['foto_juego']

		agregado = lista_biblioteca.agregar_biblioteca(id_usuario,id_juego,nombre_juego,foto_juego)

		if agregado is not False:

			#ESTADO 1: SE GUARDO CON ÉXITO
			return {

				'estado': 1
			}

		#ESTADO 2: OCURRIÓ UN ERROR	
		return {
		
			'estado': 2
		}	

@app.route('/mostrar-biblioteca', methods=['GET'])
def mostrar_biblioteca():

	if request.method == 'GET':

		return lista_biblioteca.mostrar_listado()

@app.route('/info-perfil', methods=['POST'])
def info_perfil():	

	if request.method == 'POST':

		user_id = request.json['usuario_id']

		usuario = lista_usuarios.info_usuario(int(user_id))

		if usuario is not False:

			return {

				'data': usuario,
				'estado': 1
			}

		return {

			'estado': 2
		}

@app.route('/modificar-perfil', methods=['POST'])
def modificar_perfil():	

	if request.method == 'POST':

		u_id = request.json['id']
		nombre = request.json['nombre']
		apellido = request.json['apellido']
		user = request.json['usuario']
		passw = request.json['password']
		conf_passw = request.json['conf_password']

		if passw == conf_passw:

			usuario = lista_usuarios.modificar_usuario(int(u_id),nombre,apellido,user,passw)

			if usuario is not False:

				#SE MODIFICO EL USUARIO
				return {

					"data": usuario,
					"estado": 1

				}

			#OCURRIÓ UN ERROR
			return {

				"estado": 2
			}	

		#LAS CONTRASEÑAS NO SON IGUALES	
		return {
		
			"estado": 3
		}	
		
@app.route('/mostrar-usuarios', methods=['GET'])
def mostrar_usuarios():

	if request.method == 'GET':

		return lista_usuarios.mostrar_listado()

@app.route('/categorias', methods=['GET'])
def categorias():

	if request.method == 'GET':

		listado = lista_videojuegos.mostrar_categorias()

		return {

			"listado": listado
		}

@app.route('/comentarios', methods=['POST'])
def comentarios():

	if request.method == 'POST':

		videojuego = request.json['videojuego']
		usuario = request.json['usuario']
		comentario = request.json['comentario']

		agregado = lista_comentarios.agregar_comentario(videojuego,usuario,
			comentario)

		if agregado is not False:

			#ESTADO 1: SE GUARDO CON ÉXITO
			return {

				'estado': 1
			}

		#ESTADO 2: OCURRIÓ UN ERROR	
		return {
		
			'estado': 2
		}

@app.route('/mostrar-comentarios', methods=['GET'])
def mostrar_comentarios():

	if request.method == 'GET':

		return lista_comentarios.mostrar_listado()		

@app.route('/eliminar-juego', methods=['POST'])
def eliminar_juego():

	if request.method == 'POST':

		id = request.json['id']

		respuesta = lista_videojuegos.eliminar_videojuego(int(id))

		if respuesta is not False:

			return {

			'data': respuesta,
			'estado': 1

			}

		return {
		
			'estado': 2
		}	

		
@app.route('/', methods=['GET'])
def index():

	return "<H1>BACKEND DE MORE GAMES STORE</H1>"

if __name__ == "__main__":
	app.run(threaded=True, port=5000,debug=True)		