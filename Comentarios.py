
class Comentarios:

	def __init__(self, videojuego, usuario, comentario):

		self.videojuego = videojuego
		self.usuario = usuario
		self.comentario = comentario

	#MÉTODOS GET
	def getVideojuego(self):
		return self.videojuego

	def getUsuario(self):
		return self.usuario

	def getComentario(self):
		return self.comentario

	#MÉTODOS SET
	def setVideojuego(self, videojuego):
		self.videojuego = videojuego	
		
	def setUsuario(self, usuario):
		self.usuario = usuario

	def setComentario(self, comentario):
		self.comentario = comentario	

	#DUMP
	def dump(self):

		return {

			'videojuego' : self.videojuego,
			'usuario': self.usuario,
			'comentario': self.comentario

		}	
			
		