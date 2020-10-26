
class Videojuegos:

	def __init__(self,id,nombre,anio,precio,categoria1,categoria2,categoria3,foto,banner,descripcion):

		self.id = id
		self.nombre = nombre 
		self.anio = anio
		self.precio = precio
		self.categoria1 = categoria1
		self.categoria2 = categoria2
		self.categoria3 = categoria3
		self.foto = foto
		self.banner = banner
		self.descripcion = descripcion

	def dump(self):

		return {

			'id': self.id,
			'nombre': self.nombre,
			'anio': self.anio,
			'precio': self.precio,
			'categoria 1': self.categoria1,
			'categoria 2': self.categoria2,
			'categoria 3': self.categoria3,
			'foto': self.foto,
			'banner': self.banner,
			'descripcion': self.descripcion
		}
		



