import config as config
import web
import app


class Valorar():

    def __init__(self):
        pass

    def GET(self,num_as):
        app.session.num_as = num_as
        asesoria1 = config.model_asesoria.get_asesorias(num_as)
        return config.render.valorar(asesoria1) # render insert.html

    def POST(self,num_as):
        formulario = web.input() # get form data
        valor = formulario['valor']
        asesoria = app.session.num_as
        estado = 'calificado'
        config.model_valoracion.insert_valoracion(valor,asesoria)
        config.model_asesoria.update_asesoria(asesoria,estado)
        raise web.seeother('/index_asesoria') # redirecciona el HTML