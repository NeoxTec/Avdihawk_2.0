# -*- coding:utf-8 -*-
import web
import application.models.model_asesoria as model_asesoria  # importa el model de personas
import application.models.model_asesor as model_asesor
import application.models.model_valoracion as model_valoracion
render = web.template.render('application/views/asesoria/', base='master') # configura la ubicación de las vistas