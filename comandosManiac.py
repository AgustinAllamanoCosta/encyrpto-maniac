#!/usr/bin/env python
# -*- coding: utf-8 -*
from CustomException import *
from constantesEncriptoManiac import *
from encriptoManiac import *
from os import system

class Comando(object):

	def __init__(self):
		self.encriptoManiac = EncriptoManiac()

class ComandoConsola(Comando):

	def ejecutar(self,parametros):
		return None

	def validarParametros(self,parametros):
		if(parametros == []):
			raise ParametrosComandosNullos()

class ComandoConsolaSinParametros(Comando):
	
	def ejecutar(self):
		return None

class ComandoAgregar(ComandoConsola):

	def ejecutar(self,parametros):
		super().validarParametros(parametros)
		if(len(parametros)==1):
			raise ParametrosComandoIncompletos(ConstanteConsola.mensajeAyudaComandoAgregar)
		else:
			if(self.encriptoManiac.existeCuentaEnBase(parametros[0]) != True):
				self.encriptoManiac.ingresarClave(parametros[0],parametros[1])
			else:
				raise CuentaEnBaseDuplicadaException(parametros[0])
		return None

class ComandoModificar(ComandoConsola):
	
	def ejecutar(self,parametros):
		super().validarParametros(parametros)
		if(len(parametros)==1):
			raise ParametrosComandoIncompletos(ConstanteConsola.mensajeAyudaComandoAgregar)
		else:
			self.encriptoManiac.actualizarClave(parametros[0],parametros[1])	
		return None

class ComandoEliminar(ComandoConsola):
	
	def ejecutar(self,parametros):
		super().validarParametros(parametros)
		self.encriptoManiac.eliminarClave(parametros[0])
		return None

class ComandoMostrar(ComandoConsola):
	
	def ejecutar(self,parametros):
		super().validarParametros(parametros)
		return self.encriptoManiac.buscarClave(parametros[0])

class ComandoAyuda(ComandoConsola):

	def __init__(self):
		self.mensajeAyuda = {
		'listar': ConstanteConsola.mensajeAyudaComandoListar,
		'agregar':ConstanteConsola.mensajeAyudaComandoAgregar,
		'exit':ConstanteConsola.mensajeAyudaComandoExit,
		'mostrar':ConstanteConsola.mensajeAyudaComandoMostrar,
		'vermas':ConstanteConsola.mensajeAyudaComandoVerMas,
		'eliminar':ConstanteConsola.mensajeAyudaComandoEliminar,
		'modificar':ConstanteConsola.mensajeAyudaComandoModificar
		}

	def ejecutar(self,parametros):
		super().validarParametros(parametros)
		return self.mensajeAyuda[parametros[0]]

class ComandoListar(ComandoConsolaSinParametros):

	def ejecutar(self):
		return self.encriptoManiac.listarCuentas()

class ComandoExit(ComandoConsolaSinParametros):

	def ejecutar(self):
		raise InterrumpirConsola()

class ComandoVerMas(ComandoConsolaSinParametros):

	def __init__(self):
		pass

	def ejecutar(self):
		return ConstanteConsola.mensajeComandosAvanzados

class ComandoUnix(ComandoConsolaSinParametros):
	def __init__(self):
		pass

	def ejecutar(self):
		system('clear')

class ComandoWin(ComandoConsolaSinParametros):
	def __init__(self):
		pass

	def ejecutar(self):
		system('cls')