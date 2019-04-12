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
    
    def GET(self,asesor):
        session_user = app.session.user
        session_privilege = app.session.tipo
        session_picture = app.session.picture
        app.session.asesor = asesor
        params = {}
        params['user'] = session_user
        params['tipo'] = session_privilege
        params['picture'] = session_picture
        params['asesor'] = app.session.asesor
        print app.session.asesor
        asesor = config.model_asesor.get_asesor(asesor) # Selecciona el registro que coincida con el nombre
        return config.render.perfil_asesor(asesor,params) # Envia el registro y renderiza el view.html
