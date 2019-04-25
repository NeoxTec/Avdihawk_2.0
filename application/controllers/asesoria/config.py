# -*- coding:utf-8 -*-
import web
import application.models.model_asesoria as model_asesoria  # importa el model de personas
import application.models.model_asesor as model_asesor
import application.models.model_valoracion as model_valoracion
import application.models.model_evaluacion_asesor as model_evaluacion_asesor
import application.models.model_evaluacion_alumno as model_evaluacion_alumno
import application.models.model_users as model_users
render = web.template.render('application/views/asesoria/', base='master') # configura la ubicación de las vistas