# -*- coding:utf-8 -*-
import web 
import config as config
import app
"""
    Clase de Index la cual permite mandar los registros de los clientes al frontend
"""
class Reporte:
    def __init__(self):
        pass

    def GET(self,num_as):
        app.session.num_as = num_as
        asesoria = config.model_asesoria.get_asesorias(num_as)
        reporte = config.model_evaluacion_alumno.get_reporte_asesor(num_as)
        nombre = config.model_users.get_nombre(asesoria.solicitante)
        return config.render.reporte_asesor(asesoria,reporte,nombre.nombre) # render evaluacion_asesor.html
