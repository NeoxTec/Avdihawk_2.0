# -*- coding:utf-8 -*-
import web
import config as config
import app
"""
    Clase para mostrar cada campo a detalle de los registros en el index
"""
class Perfil():
    def __init__(self):
        pass
    
    def GET(self,id_as):
        session_user = app.session.user
        session_privilege = app.session.tipo
        session_picture = app.session.picture
        app.session.asesor = id_as
        params = {}
        params['user'] = session_user
        params['tipo'] = session_privilege
        params['picture'] = session_picture
        params['asesor'] = id_as
        params['asesor'] = app.session.asesor
        print app.session.asesor
        perfil = config.model_asesor.select_id_as(id_as) # Selecciona el registro que coincida con el nombre
        return config.render.perfil_asesor(perfil,params) # Envia el registro y renderiza el view.html
