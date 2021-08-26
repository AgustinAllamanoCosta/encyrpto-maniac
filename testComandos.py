#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from comandosManiac import *
from encriptoManiac import *

class TestComandosManiac(unittest.TestCase):

	def setUp(self):
		self.funcionesOriginales = {
			'ingresarClave': EncriptoManiac.ingresarClave,
			'actualizarClave': EncriptoManiac.actualizarClave,
			'eliminarClave': EncriptoManiac.eliminarClave
		}

	def tearDown(self):
		EncriptoManiac.ingresarClave = self.funcionesOriginales['ingresarClave']
		EncriptoManiac.actualizarClave = self.funcionesOriginales['actualizarClave']
		EncriptoManiac.eliminarClave = self.funcionesOriginales['eliminarClave']

	def test_dadoQueSeLlamaAlComandoAgregarConParametrosDeNombreDeCuentaYContraseniaSeVerificaQueSeLlamaALaFuncionIngresarClave(self):
		self.dadoQueSeLlamaAlComandoAgregar().conParametros(['slack','123'])
		self.cuandoSeLlamanALaFuncionEjecutarDelComandoAgregar()
		self.seVerificaQueSeLlamaALaFuncionIngresarClave()

	def test_dadoQueSeLlamaAlComandoModificarConParametrosNombreDeCuentaYContraseñaSeVerifiacaQueSeLlamaALaFuncionActualizarClave(self):
		self.dadoQueSeLlamaAlComandoActualizarClave().conParametros(['slack','456'])
		self.cuandoSeLlamanALaFuncionEjecutarDelComandoActualizarClave()
		self.seVerificaQueSeLlamaALaFuncionActualizarClave()

	def test_dadoQueSeLlamaAlComandoEliminarConParametrosNombreDeCuentaSeVerifiacaQueSeLlamaALaFuncionEliminarClave(self):
		self.dadoQueSeLlamaAlComandoEliminarClave().conParametros(['slack'])
		self.cuandoSeLlamanALaFuncionEjecutarDelComandoEliminarClave()
		self.seVerificaQueSeLlamaALaFuncionEliminarClave()

	def dadoQueSeLlamaAlComandoAgregar(self):
		self.comando = ComandoAgregar()
		return self

	def dadoQueSeLlamaAlComandoActualizarClave(self):
		self.comando = ComandoModificar()
		return self

	def dadoQueSeLlamaAlComandoEliminarClave(self):
		self.comando = ComandoEliminar()
		return self

	def conParametros(self,parametros):
		self.parametroComando = parametros

	def cuandoSeLlamanALaFuncionEjecutarDelComandoAgregar(self):
		self.seEjecutoIngresarClave = False
		EncriptoManiac.ingresarClave = self.observadorIngresarClave
		self.comando.ejecutar(self.parametroComando)

	def cuandoSeLlamanALaFuncionEjecutarDelComandoActualizarClave(self):
		self.seEjecutoActualizarClave = False
		EncriptoManiac.actualizarClave = self.observadorActualizarClave
		self.comando.ejecutar(self.parametroComando)

	def cuandoSeLlamanALaFuncionEjecutarDelComandoEliminarClave(self):
		self.seEjecutoEliminarClave = False
		EncriptoManiac.eliminarClave = self.observadorEliminarClave
		self.comando.ejecutar(self.parametroComando)

	def observadorActualizarClave(self,param1,param2):
		self.seEjecutoActualizarClave = True

	def observadorIngresarClave(self,param1,param2):
		self.seEjecutoIngresarClave = True

	def observadorEliminarClave(self,parametro):
		self.seEjecutoEliminarClave = True

	def seVerificaQueSeLlamaALaFuncionIngresarClave(self):
		assert self.seEjecutoIngresarClave == True

	def seVerificaQueSeLlamaALaFuncionActualizarClave(self):
		assert self.seEjecutoActualizarClave == True

	def seVerificaQueSeLlamaALaFuncionEliminarClave(self):
		assert self.seEjecutoEliminarClave == True

if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(TestComandosManiac)
	unittest.TextTestRunner(verbosity=2).run(suite)