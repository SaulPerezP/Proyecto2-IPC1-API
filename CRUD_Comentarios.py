
from Comentarios import Comentarios
import json

class CRUD_Comentarios:

	def __init__(self):

		self.listaComentarios = []

	def agregar_comentario(self, videojuego, usuario, comentario):

		self.listaComentarios.append(Comentarios(videojuego, usuario,
		 	comentario))
	
		print("Se agrego un nuevo comentario sobre el videojuego: " + videojuego)


	def mostrar_listado(self):

		return json.dumps([mostrar.dump() for mostrar in self.listaComentarios])	