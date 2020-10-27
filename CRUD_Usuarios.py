from Usuarios import Usuarios
import json

class CRUD_Usuarios:

	def __init__(self):

		self.listaUsuarios = []
		self.contador = 0

	def agregar_usuario(self, nombre, apellido, usuario, passw):

		for user in self.listaUsuarios:

			if user.getUsuario() == usuario:

				print("El Usuario: " + usuario + " ya existe en el sistema")	
				return False

		self.listaUsuarios.append(Usuarios(self.contador,nombre,apellido,usuario,passw))
		self.contador += 1

		print("Se registro el Usuario: " + usuario)	
		return True

	def validar_usuario(self,usuario,passw):

		for user in self.listaUsuarios:

			if user.getUsuario() == usuario and user.getPassword() == passw:

				return user

		return False	

	def mostrar_usuarios(self):

		return json.dumps([user.dump() for user in self.listaUsuariosl])
		



