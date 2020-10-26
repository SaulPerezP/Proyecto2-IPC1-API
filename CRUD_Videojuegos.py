
from Videojuegos import Videojuegos
import json

class CRUD_Videojuegos:

	def __init__(self):

		self.listaVideojuegos = []
		self.contador = 0

	def agregar_videojuego(self,nombre,anio,precio,categoria1,categoria2,categoria3,foto,banner,
		descripcion):
		
		self.listaVideojuegos.append(Videojuegos(self.contador,nombre,anio,precio,categoria1,categoria2,categoria3,
			foto,banner,descripcion))	

		self.contador += 1

	def mostrar_todos(self):
		
		return json.dumps([videojuego.dump() for videojuego in self.listaVideojuegos])	

	def info_videojuego(self,id):
		
		for videojuego in self.listaVideojuegos:

			if videojuego.id == id:
				return videojuego.dump()

		return None		



