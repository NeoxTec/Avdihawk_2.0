import config as config
import web
import app


class Evaluar():

    def __init__(self):
        pass

    def GET(self,num_as):
        app.session.num_as = num_as
        asesoria = config.model_asesoria.get_asesorias(num_as)
        nombre = config.model_users.get_nombre(asesoria.asesor)
        return config.render.evaluacion_alumno(asesoria,nombre.nombre) # render evaluacion.html

    def POST(self,num_as):
        formulario = web.input() # get form data
        horas = formulario['horas']
        asistencia = formulario['asistencia']
        comprension = formulario['comprension']
        razon = formulario['razon']
        observaciones = formulario['observaciones']
        calificacion = formulario['calificacion']
        gusto = formulario['gusto']
        estado = 'calificado'
        asesoria = app.session.num_as
        print "horas:",horas
        print "asistencia:", asistencia
        print "comprension:", comprension
        print "razon:", razon
        print "observaciones:", observaciones
        print "calificacion", calificacion
        print "gusto:", gusto 
        config.model_evaluacion_asesor.insert_evaluacion_asesor(asesoria,horas,asistencia,comprension,razon,observaciones,calificacion,gusto)
        evaluacion = config.model_evaluacion_alumno.alumno_evaluado(asesoria)
        if evaluacion == 1:
            config.model_asesoria.update_asesoria(asesoria,estado)
        raise web.seeother('/index_asesoria') # redirecciona el HTML