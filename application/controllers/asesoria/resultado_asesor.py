import config as config
import web
import app

class Resultado():

    def __init__(self):
        pass

    def GET(self,num_as):
        app.session.num_as = num_as
        asesoria = config.model_asesoria.get_asesorias(num_as)
        reporte = config.model_evaluacion_asesor.get_reporte_alumno(num_as)
        nombre = config.model_users.get_nombre(asesoria.solicitante)
        print "solicitante:",nombre.nombre
        return config.render.resultado_asesor(asesoria,reporte,nombre.nombre) # Envia todos los registros y renderiza index.html