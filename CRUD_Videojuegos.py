
from Videojuegos import Videojuegos
import json

class CRUD_Videojuegos:

	def __init__(self):

		self.listaVideojuegos = []
		self.listaCategorias = []
		self.listaCategorias.append("Multijugador")
		self.listaCategorias.append("Carreras")
		self.listaCategorias.append("Automóviles")
		self.listaCategorias.append("Deporte")
		self.listaCategorias.append("Fútbol")
		self.listaCategorias.append("Aventura")
		self.listaCategorias.append("Supervivencia")
		self.contador = 0

	def agregar_videojuego(self,nombre,anio,precio,categoria1,categoria2,categoria3,foto,banner,
		descripcion):
		
		self.listaVideojuegos.append(Videojuegos(self.contador,nombre,anio,precio,categoria1,categoria2,
			categoria3,foto,banner,descripcion))

		self.contador += 1

		print("Se registro el Videojuego: " + nombre)	

		return True

	def mostrar_todos(self):
		
		return json.dumps([videojuego.dump() for videojuego in self.listaVideojuegos])	

	def info_individual(self,id):
		
		for videojuego in self.listaVideojuegos:

			if videojuego.id == id:
				
				return videojuego.dump()

		return None	

	def lista_categorias(self,categoria):

		for listado in self.listaCategorias:

			if listado == categoria or categoria == '':

				return False
				
		self.listaCategorias.append(categoria)		

	def mostrar_categorias(self):

		self.listaCategorias.sort()

		return self.listaCategorias
	
	def modificar_videojuego(self,id,nombre,anio,precio,categoria1,categoria2,categoria3,
		foto,banner,descripcion):

		for videojuego in self.listaVideojuegos:

			if videojuego.getId() == id:

				videojuego.setNombre(nombre)
				videojuego.setAnio(anio)
				videojuego.setPrecio(precio)
				videojuego.setCategoria1(categoria1)
				videojuego.setCategoria2(categoria2)
				videojuego.setCategoria3(categoria3)
				videojuego.setFoto(foto)
				videojuego.setBanner(banner)
				videojuego.setDescripcion(descripcion)
	
				return videojuego.dump()

		return False	
			
	def eliminar_videojuego(self,id):

		self.listaVideojuegos.pop(id)

		return True

	





	



	
		



			



		



			



