# -*- coding:utf-8 -*-
import web
import config as config
import app
import time
import datetime
from datetime import date
hoy = date.today()

"""
    Clase para insertar registros a la base de datos por medio de un formulario en la webapp
"""
class Insert:

    def __init__(self):
        pass
    
    def GET(self):
        message = app.session.message
        return config.render.insert_asesoria(message) # renderiza la pagina insert.html
    
    def POST(self):
        session_user = app.session.user
        id_as = app.session.id_as
        formulario = web.input() # almacena los datos del formulario
        dia = formulario['dia'] # almacena el dia seleccionado en el input
        hora = formulario['hora'] # almacena el nombre escrito en el input
        tema = formulario ['tema'] # almacena el telefono escrito en el input
        asesor = config.model_asesor.select_correo(id_as)
        print id_as
        print asesor.correo
        print hora
        print hoy
        print time.strftime("%H:%M")
        if str(dia) < str(hoy):
            app.session.message = "El dia es incorrecto, no puedes ingresar día anterior al actual"
            raise web.seeother('/insert_asesoria')
        elif str(hora) < time.strftime("%H:%M"):
            app.session.message = "La hora es incorrecta, no puedes ingresar un horario anterior al actual"
            raise web.seeother('/insert_asesoria')
        else:
            app.session.message = "Su asesoría ha sido registrada exitosamente"
            config.model_asesoria.insert_asesoria(dia,hora,session_user,asesor.correo,tema) # llama al metodo insert_cliente y le pasa los datos guardados 
            raise web.seeother('/insert_asesoria') # redirecciona el HTML 