import config as config
import web
import app


class Resultado():

    def __init__(self):
        pass

    def GET(self,num_as):
        app.session.num_as = num_as
        asesoria = config.model_asesoria.get_asesorias(num_as)
        reporte = config.model_evaluacion_alumno.get_reporte_asesor(num_as)
        nombre = config.model_users.get_nombre(asesoria.asesor)
        return config.render.valorar(asesoria,reporte,nombre.nombre) # Envia todos los registros y renderiza index.html