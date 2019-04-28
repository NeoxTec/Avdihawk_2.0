# -*- coding:utf-8 -*-
import web
import config as config
import app
"""
    Clase para mostrar cada campo a detalle de los registros en el index
"""
class Reporte():
    def __init__(self):
        pass

    def GET(self,num_as):
        app.session.num_as = num_as
        asesoria = config.model_asesoria.num_as(num_as)
        return config.render.reporte_motivo(asesoria)