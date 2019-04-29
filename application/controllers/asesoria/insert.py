# -*- coding:utf-8 -*-
import web
import config as config
import app
import time
import datetime
from datetime import date
from datetime import timedelta
from datetime import time
from datetime import datetime
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
        ahora =  datetime.now()
        hora_actual = time(ahora.hour,ahora.minute)
        #hora_actual = time.strftime("%H:%M") 
        print id_as
        print asesor.correo
        print hora
        print hoy
        print dia
        if app.remote == True:
            mas = ahora - timedelta(hours=5)
            hora_actual = time(mas.hour,mas.minute)
        print "dia",ahora.day
        if dia < str(hoy):
            app.session.message = "El dia es incorrecto, no puedes ingresar día anterior al actual"
            raise web.seeother('/insert_asesoria')
        elif str(hora) < str(hora_actual):
            app.session.message = "La hora es incorrecta, no puedes ingresar un horario anterior al actual"
            raise web.seeother('/insert_asesoria')
        else:
            app.session.message = "Su asesoría ha sido registrada exitosamente"
            config.model_asesoria.insert_asesoria(dia,hora,session_user,asesor.correo,tema) # llama al metodo insert_cliente y le pasa los datos guardados 
            raise web.seeother('/insert_asesoria') # redirecciona el HTML 