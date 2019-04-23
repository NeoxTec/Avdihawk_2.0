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
        app.session.id_as = id_as
        params = {}
        params['id_as'] = id_as
        perfil = config.model_asesor.select_id_as(id_as) # Selecciona el registro que coincida con el nombre
        user = perfil.correo
        print "Usuario" ,user
        foto = config.model_users.get_picture(user)
        print foto
        return config.render.perfil_asesor(perfil,foto) # Envia el registro y renderiza el view.html
