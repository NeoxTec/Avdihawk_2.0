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
        reporte = config.model_evaluacion_asesor.get_reporte_alumno(num_as)
        nombre = config.model_users.get_nombre(asesoria.asesor)
        return config.render.reporte_alumno(asesoria,reporte,nombre.nombre) # Envia todos los registros y renderiza index.html