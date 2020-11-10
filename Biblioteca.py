
class Biblioteca:

	def __init__(self,id_usuario,id_juego,nombre_juego,foto_juego):

		self.id_usuario = id_usuario
		self.id_juego = id_juego
		self.nombre_juego = nombre_juego
		self.foto_juego = foto_juego

	#MÉTODOS GET	
	def getId_usuario(self):
		return self.id_usuario

	def getId_juego(self):
		return self.id_juego

	def getNombre_juego(self):
		return self.nombre_juego

	def getFoto_juego(self):
		return self.foto_juego

	def dump(self):
	
		return {

			'id_usuario' : self.id_usuario,
			'id_juego': self.id_juego,
			'nombre_juego': self.nombre_juego,
			'foto_juego': self.foto_juego

		}		





