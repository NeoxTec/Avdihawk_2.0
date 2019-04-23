# -*- coding:utf-8 -*-
import web 
import config as config
"""
    Clase de Index la cual permite mandar los registros de los clientes al frontend
"""
class Reporte:
    def __init__(self):
        pass

    def GET(self):
        return config.render.reporte_alumno() # Envia todos los registros y renderiza index.html