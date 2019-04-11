import application.controllers.main.config as config
import datetime
import app


class Index:
    
    def __init__(self):
        pass


    @staticmethod
    def GET():
        if app.session.loggedin is True:
            # get now time
            now = datetime.datetime.now()
            now_str = str(now).split('.')[0]

            expires = config.check_secure_val(app.session.expires)

            print "now    : " , now_str
            print "expires: " , expires

            if (now_str > expires): # compare now with time login
                raise config.web.seeother('/logout')

            session_user = app.session.user
            session_privilege = app.session.tipo
            session_picture = app.session.picture
            params = {}
            params['user'] = session_user
            params['tipo'] = session_privilege
            params['picture'] = session_picture
            if session_privilege == 0:
                return config.render.asesor(params)
            elif session_privilege == 1:
                return config.render.estandar(params)
         
        else:
            params = {}
            params['user'] = " "
            params['tipo'] = '-1'
            params['picture'] = None
            return config.render.principal(params)
