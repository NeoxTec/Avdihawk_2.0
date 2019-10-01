# -*- coding:utf-8 -*-
import web
import config as config
import app

class Editar():
    def __init__(self):
        pass

    def GET(self,num_as):
        session_user = app.session.user
        session_picture = app.session.picture
        params = {}
        params['user'] = session_user
        params['picture'] = session_picture
        return config.render.index_asesor(params)
