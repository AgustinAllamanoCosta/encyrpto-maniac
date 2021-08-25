#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from consolaEncriptoManiac import *
import threading as t
from os import system

class TestConsolaManiac(unittest.TestCase):

	def setUp(self):
		self.funcionesOriginales = {
			'ComandoModificar': ComandoModificar.ejecutar,
			'ComandoAgregar': ComandoAgregar.ejecutar,
			'ComandoListar': ComandoListar.ejecutar,
			'ComandoVerMas': ComandoVerMas.ejecutar,
			'ComandoExit' : ComandoExit.ejecutar,
			'ComandoEliminar' : ComandoEliminar.ejecutar,
			'ComandoMostrar' : ComandoMostrar.ejecutar
		}

	def tearDown(self):
		ComandoModificar.ejecutar = self.funcionesOriginales['ComandoModificar']
		ComandoAgregar.ejecutar = self.funcionesOriginales['ComandoAgregar']
		ComandoListar.ejecutar = self.funcionesOriginales['ComandoListar']
		ComandoVerMas.ejecutar = self.funcionesOriginales['ComandoVerMas']
		ComandoExit.ejecutar = self.funcionesOriginales['ComandoExit']
		ComandoEliminar.ejecutar = self.funcionesOriginales['ComandoEliminar']
		ComandoMostrar.ejecutar = self.funcionesOriginales['ComandoMostrar']

	def test_dadoQueTengoUnContextoDeLaConsolaSeVerificaQueSeMuestraElMensajeDeBienvenida(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeSaleDelContextoAlIniciar();
		self.cuandoSeInicia()
		self.seVerificaQueSeMuestraElMensajeDeBienvenida()

	def test_dadoQueTengoUnContextoCuadnoSeIniciaLaConsolaSeVerificaQueSeMuestrasLaListaDeComandosbasicos(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeSaleDelContextoAlIniciar();
		self.cuandoSeInicia()
		self.seVerificaQueSeMuestrasLaListaDeComandosbasicos()

	def test_dadoQueTengoUnContextoCundoSeIngresaElComandoAgregarSeVerificaQueSeEjecutaLaFuncionAgregarCuenta(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutaElComandoAgregar()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada() 
		self.seVerificaQueSeLlamaALaFuncionAgregar()

	def test_dadoQueTengoUnContextoCuandoSeIngresaElComandoAgregarSinParametroSeVerificaQueSeMuestraElMensajeDeError(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutaElComandoAgregarSinParametros()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaQueSeMuestraElMensajeDeError()

	def test_dadoQueTengoUnContextoCuandoSeIngresaElComandoAgregarConUnSoloParametroSeVerificaMuestraElMensajeDeAyudaDelComando(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutaElComandoAgregarConUnParametro()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaMuestraElMensajeDeAyudaDelComando()

	def test_dadoQueTengoUnContextoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoListarSeVerificaQueSeLlamaALaFuncionListar(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutaElComandoListar()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaQueSeLlamaALaFuncionListar()

	def test_dadoQueTengoUnContextoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoVerMasSeListanElRestoDeLosComandos(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutaElComandoVerMas()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaQueSeListanElRestoDeLosComandos()
	
	def test_dadoQueTengoUnContextoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoModificarSeVerificaQueSeLlamaALaFuncionComandoModificar(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutarElComandoModificar()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerifiacaQueSeLlamaALaFuncionComandoModificar()

	def test_dadoQueTengoUnContextoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoModificarSinElParametroSeVerificaQueSeMuestraElMensajeDeError(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutarElComandoModificarSinElParametro()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaQueSeMuestraElMensajeDeError()

	def test_dadoQueTengoUnContextoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoEliminarSeVerirficaQueSeLlamaALaFuncion(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutarElComandoEliminar()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerifiacaQueSeLlamaALaFuncionComandoEliminar()

	def test_dadoQueTengoUnContextoCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoEliminarSinParametrosSeVerirficaQueSeMuestraElMensajeDeError(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutarElComandoEliminarSinParametros()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaQueSeMuestraElMensajeDeError()

	def test_dadoQueTengoUnContextoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoMostrarrSeVerirficaQueSeLlamaALaFuncion(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutaElComandoMostrar()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerficaQueSeLlamaALaFuncionMostrar()

	def test_dadoQueTengoUnContextoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoMostrarrSinParametrosSeVerirficaQueSeMuestraElMensajeDeError(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutaElComandoMostrarSinParametro()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaQueSeMuestraElMensajeDeError()

	def test_dadoQueTengoUnContextoConCuentasAgregadasEnLaBaseCuandoSeIngresaUnComandoQueNoExisteSeVerificaQueSeMuestraElMensajeDeComandosAvanzados(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueIngresaUnComandoQueNoExiste()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaQueSeListanElRestoDeLosComandos()

	def test_dadoQueTengoUnContextoCuandoSeEnviaUnComandoEnMayusculaLoEjecutoIgual(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEnviaUnComandoEnMayuscula()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaQueSeEjecutaIgual()	

	def test_dadoQueEstoyTrabajandoEnSistemaUnixCuandoSeInstanciaUnaConsolaDesdeElFactorySeVerificaQueSeCarganLosComandosDeUnixDeSystema(self):
		self.dadoQueEstoyTrabajandoiEnSistemasUnix()
		self.dadoQueSeInstanciaUnaConsolaDesdeElFactoryDeConsolas()
		self.seVerificaQueSeCarganLosComandosDeSystemaUnix()

	def test_dadoQueEstoyTrabajandoEnSistemaWinCuandoSeInstanciaUnaConsolaDesdeElFactorySeVerificaQueSeCarganLosComandosDeUnixDeSystema(self):
		self.dadoQueEstoyTrabajandoiEnSistemasWin()
		self.dadoQueSeInstanciaUnaConsolaDesdeElFactoryDeConsolas()
		self.seVerificaQueSeCarganLosComandosDeSystemaWin()

	def dadoQueSeTieneUnContexto(self):
		self.consola = ConsolaEncryptoManiac()	

	def dadoQueSeSaleDelContextoAlIniciar(self):
		ConsolaEncryptoManiac.ingresarEntradas = lambda x :'exit'
		self.consolaEnParalelo =  HiloQueSePuedeDetener(target=self.consola.bucleDeConsola,daemon=True)		

	def dadoQueSeEjecutaElComandoAgregarSinParametros(self):
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : 'agregar'

	def dadoQueSeEjecutaElComandoAgregarConUnParametro(self):
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : 'agregar slack'

	def dadoQueSeEjecutaElComandoAgregar(self):
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : 'agregar slack 1234'
		ComandoAgregar.ejecutar = self.observadorFuncionAgregar

	def dadoQueSeEjecutaElComandoListar(self):
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : 'listar'
		ComandoListar.ejecutar = self.observadorFuncionListar

	def dadoQueSeEjecutaElComandoVerMas(self):
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : 'vermas'

	def dadoQueSeEjecutarElComandoModificar(self):
		ConsolaEncryptoManiac.ingresarEntradas = lambda x :'modificar slack'
		ComandoModificar.ejecutar = self.observadorFuncionModificar

	def dadoQueSeEjecutarElComandoModificarSinElParametro(self):		
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : 'modificar'

	def dadoQueSeEjecutarElComandoEliminar(self):		
		ConsolaEncryptoManiac.ingresarEntradas = lambda x :'eliminar slack'
		ComandoEliminar.ejecutar = self.observadorFuncionEliminar
	
	def dadoQueSeEjecutarElComandoEliminarSinParametros(self):		
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : 'eliminar'

	def dadoQueSeEjecutaElComandoMostrar(self):		
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : 'mostrar slack'
		ComandoMostrar.ejecutar = self.observadorFuncionMostrar

	def dadoQueSeEjecutaElComandoMostrarSinParametro(self):		
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : 'mostrar'

	def dadoQueIngresaUnComandoQueNoExiste(self):		
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : 'asdasdasdsa'

	def dadoQueSeEnviaUnComandoEnMayuscula(self):
		ConsolaEncryptoManiac.ingresarEntradas = lambda x :'MOSTRAR'
		ComandoMostrar.ejecutar = self.observadorFuncionMostrar

	def dadoQueEstoyTrabajandoiEnSistemasUnix(self):
		self.plataform = 'Unix'

	def dadoQueEstoyTrabajandoiEnSistemasWin(self):
		self.plataform = 'Win32'

	def dadoQueSeInstanciaUnaConsolaDesdeElFactoryDeConsolas(self):
		self.consola = FactoryConsolaEncriptoManiac().obtenerConsola(self.plataform)

	def observadorFuncionListar(self,arg):
		self.seEjecutoListar = True

	def observadorFuncionEliminar(self,arg):
		self.seEjecutoEliminar = True

	def observadorFuncionMostrar(self,arg):
		self.seEjecutoMostrar = True

	def observadorFuncionModificar(self,arg):
		self.seEjecutoModificar = True

	def observadorFuncionAgregar(self,arg):
		self.seEjecutoAgregar = True

	def cuandoSeInicia(self):
		self.consolaEnParalelo.start()

	def cuandoSeLlamaALaFuncionAnalizarEntrada(self):
		self.consola.analizarEntrada(self.consola.ingresarEntradas())

	def seVerificaQueSeMuestraElMensajeDeBienvenida(self):
		self.consolaEnParalelo.stop()
		self.consolaEnParalelo.join()
		assert self.consola.obtenerHistorial()[0] == ConstanteConsola.mensajeBienvenida

	def seVerificaQueSeMuestrasLaListaDeComandosbasicos(self):
		self.consolaEnParalelo.stop()
		self.consolaEnParalelo.join()
		assert self.consola.obtenerHistorial()[1] == ConstanteConsola.mensajeComandosBasicos

	def seVerificaQueSeLlamaALaFuncionListar(self):
		assert self.seEjecutoListar == True 

	def seVerificaQueSeListanElRestoDeLosComandos(self):
		assert self.consola.obtenerHistorial()[1] == ConstanteConsola.mensajeComandosAvanzados

	def seVerifiacaQueSeLlamaALaFuncionComandoModificar(self):
		assert self.seEjecutoModificar == True

	def seVerificaQueSeLlamaALaFuncionAgregar(self):
		assert self.seEjecutoAgregar == True

	def seVerificaQueSeMuestraElMensajeDeError(self):
		assert self.consola.obtenerHistorial()[1] == ConstanteConsola.mensajeErrorComandoParametros

	def seVerificaMuestraElMensajeDeAyudaDelComando(self):
		assert self.consola.obtenerHistorial()[1] == ConstanteConsola.mensajeAyudaComandoAgregar		

	def seVerifiacaQueSeLlamaALaFuncionComandoEliminar(self):
		assert self.seEjecutoEliminar == True

	def seVerficaQueSeLlamaALaFuncionMostrar(self):
		assert self.seEjecutoMostrar == True

	def seVerificaQueSeEjecutaIgual(self):
		assert self.seEjecutoMostrar == True

	def seVerificaQueSeCarganLosComandosDeSystemaUnix(self):
		assert isinstance(self.consola.obtenerComandos()['systema'],ComandoUnix)

	def seVerificaQueSeCarganLosComandosDeSystemaWin(self):
		assert isinstance(self.consola.obtenerComandos()['systema'],ComandoWin)

class HiloQueSePuedeDetener(t.Thread):

    def __init__(self,  *args, **kwargs):
        super(HiloQueSePuedeDetener, self).__init__(*args, **kwargs)
        self.frenarHilo = t.Event()

    def stop(self):
        self.frenarHilo.set()

    def stopped(self):
        return self.frenarHilo.is_set()

if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(TestConsolaManiac)
	unittest.TextTestRunner(verbosity=2).run(suite)