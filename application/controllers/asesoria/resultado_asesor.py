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
        return config.render.resultado_asesor(asesoria,reporte) # Envia todos los registros y renderiza index.html