
class Usuarios:

	def __init__(self,id,nombre,apellido,usuario,password,tipo):

		self.id = id
		self.nombre = nombre 
		self.apellido = apellido
		self.usuario = usuario
		self.password = password
		self.tipo = tipo

	#MÉTODOS GET	
	def getId(self):
		return self.id

	def getNombre(self):
		return self.nombre	

	def getApellido(self):
		return self.apellido

	def getUsuario(self):
		return self.usuario	

	def getPassword(self):
		return self.password

	def getTipo(self):
		return self.tipo	

	#MÉTODOS SET
	def setId(self, id):
		self.id = id

	def setNombre(self, nombre):
		self.nombre = nombre

	def setApellido(self, apellido):
		self.apellido = apellido

	def setUsuario(self, usuario):
		self.usuario = usuario	

	def setPassword(self, password):
		self.password = password

	def setTipo(self, tipo):
		self.tipo = tipo	

	#DUMP	
	def dump(self):
	
		return {

			'id' : self.id,
			'nombre': self.nombre,
			'apellido': self.apellido,
			'usuario': self.usuario,
			'tipo': self.tipo,
			'pass': self.password
		}			

#

	





