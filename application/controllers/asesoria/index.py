# -*- coding:utf-8 -*-
import web 
import config as config
import app
"""
    Clase de Index la cual permite mandar los registros frontend
"""
class Index:
    def __init__(self):
        pass

    def GET(self):
        session_user = app.session.user
        session_privilege = app.session.tipo
        params = {}
        params['user'] = session_user
        params['tipo'] = session_privilege
        estado = False
        if params['tipo'] == 0:
            asesorias = config.model_asesoria.get_asesor(session_user)
            for row in asesorias:
                if row.estado == 'finalizado':
                    estado = True
                    asesorias = config.model_asesoria.get_asesor(session_user)
                    return config.render.index_asesoria(asesorias,params,estado) # Envia todos los registros y renderiza index.html
            else:
                asesorias = config.model_asesoria.get_asesor(session_user)
                return config.render.index_asesoria(asesorias,params,estado) # Envia todos los registros y renderiza index.html
        elif params['tipo'] == 1:
            asesorias = config.model_asesoria.get_solicitante(session_user)
            for row in asesorias:
                if row.estado == 'finalizado':
                    estado = True
                    asesorias = config.model_asesoria.get_solicitante(session_user)
                    return config.render.index_asesoria(asesorias,params,estado) # Envia todos los registros y renderiza index.html
            else:
                asesorias = config.model_asesoria.get_solicitante(session_user)
                return config.render.index_asesoria(asesorias,params,estado) # Envia todos los registros y renderiza index.html
