# -*- coding:utf-8 -*-
import web
import config as config
import app
"""
    Clase para mostrar cada campo a detalle de los registros en el index
"""
class Motivo():
    def __init__(self):
        pass

    def GET(self,num_as):
        app.session.num_as = num_as
        asesoria = config.model_asesoria.get_asesorias(num_as)
        return config.render.motivo(asesoria) # render evaluacion_asesor.html

    def POST(self,num_as):
        app.session.num_as = num_as
        formulario = web.input() # almacena los datos del formulario web
        motivo = formulario['motivo'] # almacena el telefono del input
        estado = 'rechazado'
        config.model_asesoria.update_asesoria(num_as,estado) 
        config.model_asesoria.motivo(num_as,motivo)
        raise web.seeother('/index_asesoria') # redirecciona al index