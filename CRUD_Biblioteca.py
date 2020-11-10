
from Biblioteca import Biblioteca
import json

class CRUD_Biblioteca:

	def __init__(self):

		self.listaBiblioteca = []

	def agregar_biblioteca(self,id_usuario,id_juego,nombre_juego,foto_juego):

		self.listaBiblioteca.append(Biblioteca(id_usuario,id_juego,nombre_juego,foto_juego))
	
		print("Se registro el Videojuego: " + nombre_juego + " en tu Biblioteca")


	def mostrar_listado(self):

		return json.dumps([mostrar.dump() for mostrar in self.listaBiblioteca])	
	

		
		