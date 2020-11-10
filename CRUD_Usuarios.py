from Usuarios import Usuarios
import json

class CRUD_Usuarios:

	def __init__(self):

		self.listaUsuarios = []
		self.contador = 0

	def agregar_usuario(self, nombre, apellido, usuario, passw, tipo):

		for user in self.listaUsuarios:

			if user.getUsuario() == usuario:

				print("El Usuario: " + usuario + " ya existe en el sistema")	
				return False

		self.listaUsuarios.append(Usuarios(self.contador,nombre,apellido,usuario,passw,tipo))
		self.contador += 1

		print("Se registro el Usuario: " + usuario)	
		return True

	def validar_usuario(self,usuario,passw):

		for user in self.listaUsuarios:

			if user.getUsuario() == usuario and user.getPassword() == passw:

				return user

		return False

	def recuperar_pass(self,usuario):

		for user in self.listaUsuarios:

			if user.getUsuario() == usuario:

				return user

		return False		


	def mostrar_listado(self):

		return json.dumps([user.dump() for user in self.listaUsuarios])

	def info_usuario(self, user_id):
		
		for user in self.listaUsuarios:

			if user.getId() == user_id:

				return user.dump()

		return False	
		
	def modificar_usuario(self, id, nombre, apellido, usuario, passw):

		for user in self.listaUsuarios:

			if user.getId() == id:

				user.setNombre(nombre)
				user.setApellido(apellido)
				user.setUsuario(usuario)
				user.setPassword(passw)
	
				return user.dump()

		return False		
