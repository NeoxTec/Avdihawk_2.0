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
        finalizado = False
        calificado = False
        pendiente = False
        calf_pendiente = False
        aceptado = False
        rechazado = False
        if params['tipo'] == 0:
            asesorias = config.model_asesoria.get_asesor(session_user)
            for row in asesorias:
                if row.estado == 'pendiente':
                    pendiente = True
                elif row.estado == 'aceptado':
                    aceptado = True
                elif row.estado == 'rechazado':
                    rechazado = True
                elif row.estado == 'finalizado':
                    finalizado = True
                    asesoria = row.num_as
                    evaluacion = config.model_evaluacion_alumno.alumno_evaluado(asesoria)
                    evaluacion1 = config.model_evaluacion_asesor.asesor_evaluado(asesoria)
                    print "asesor",evaluacion 
                    print "alumno",evaluacion1
                    if evaluacion == 1 and evaluacion1 == 0:
                        calf_pendiente = True
                    else:
                        calf_pendiente = False
                elif row.estado == 'calificado':
                    calificado = True
            asesorias = config.model_asesoria.get_asesor(session_user)
            print "pendiente",pendiente
            return config.render.index_asesoria(asesorias,params,aceptado,rechazado,calf_pendiente,pendiente,finalizado,calificado) # Envia todos los registros y renderiza index.html
        elif params['tipo'] == 1:
            asesorias = config.model_asesoria.get_solicitante(session_user)
            for row in asesorias:
                if row.estado == 'finalizado':
                    asesoria = row.num_as
                    finalizado = True
                    evaluacion = config.model_evaluacion_alumno.alumno_evaluado(asesoria)
                    evaluacion1 = config.model_evaluacion_asesor.asesor_evaluado(asesoria)
                    if evaluacion == 0 and evaluacion1 == 1:
                        calf_pendiente = True
                    else:
                        calf_pendiente = False
                elif row.estado == 'calificado':
                    calificado = True
            asesorias = config.model_asesoria.get_solicitante(session_user)
            return config.render.index_asesoria(asesorias,params,aceptado,rechazado,calf_pendiente,pendiente,finalizado,calificado) # Envia todos los registros y renderiza index.html

    def POST(self):
        session_user = app.session.user
        asesorias = config.model_asesoria.get_asesor(session_user)
        for row in asesorias:
            if row.estado == 'pendiente':
                formulario = web.input() # almacena los datos del formulario web
                num_as = formulario['num_as'] # almacena el num_as del input
                estado = formulario['estado']
                config.model_asesoria.update_asesoria(num_as,estado)
                raise web.seeother('/index_asesoria') # redirecciona al index
            elif row.estado == 'aceptado':
                formulario = web.input() # almacena los datos del formulario web
                num_as = formulario['num_as'] # almacena el num_as del input
                finalizado = formulario['finalizado']
                config.model_asesoria.update_asesoria(num_as,finalizado)
                raise web.seeother('/index_asesoria') # redirecciona al index
            
