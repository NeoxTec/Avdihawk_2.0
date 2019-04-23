import web
import config as config
import json


class Api_evaluacion_asesor:
    def get(self, id_e):
        try:
            # http://0.0.0.0:8080/api_evaluacion_asesor?user_hash=12345&action=get
            if id_e is None:
                result = config.model.get_all_evaluacion_asesor()
                evaluacion_asesor_json = []
                for row in result:
                    tmp = dict(row)
                    evaluacion_asesor_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(evaluacion_asesor_json)
            else:
                # http://0.0.0.0:8080/api_evaluacion_asesor?user_hash=12345&action=get&id_e=1
                result = config.model.get_evaluacion_asesor(int(id_e))
                evaluacion_asesor_json = []
                evaluacion_asesor_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(evaluacion_asesor_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            evaluacion_asesor_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(evaluacion_asesor_json)

    def evaluado(self,asesoria):
        try:
            # http://0.0.0.0:8080/api_evaluacion_asesor?user_hash=12345&action=evaluado&asesoria=1
            result = config.model.asesor_evaluado(int(asesoria))
            evaluacion_asesor_json = []
            for row in result:
                tmp = dict(row)
                evaluacion_asesor_json.append(tmp)
            web.header('Content-Type', 'application/json')
            return json.dumps(evaluacion_asesor_json, sort_keys=True, default=str)
        except Exception as e:
            print "GET Error {}".format(e.args)
            evaluacion_asesor_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(evaluacion_asesor_json)

# http://0.0.0.0:8080/api_evaluacion_asesor?user_hash=12345&action=put&id_e=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, asesoria,horas,asistencia,comprension,razon,observaciones,calificacion,gusto):
        try:
            config.model.insert_evaluacion_asesor(asesoria,horas,asistencia,comprension,razon,observaciones,calificacion,gusto)
            evaluacion_asesor_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(evaluacion_asesor_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_evaluacion_asesor?user_hash=12345&action=delete&id_e=1
    def delete(self, id_e):
        try:
            config.model.delete_evaluacion_asesor(id_e)
            evaluacion_asesor_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(evaluacion_asesor_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_evaluacion_asesor?user_hash=12345&action=update&id_e=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_e, asesoria,horas,asistencia,comprension,razon,observaciones,calificacion,gusto):
        try:
            config.model.edit_evaluacion_asesor(id_e,asesoria,horas,asistencia,comprension,razon,observaciones,calificacion,gusto)
            evaluacion_asesor_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(evaluacion_asesor_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            evaluacion_asesor_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(evaluacion_asesor_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_e=None,
            asesoria=None,
            horas=None,
            asistencia=None,
            comprension=None,
            razon=None,
            observaciones=None,
            calificacion=None,
            gusto=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_e=user_data.id_e

            asesoria=user_data.asesoria

            horas=user_data.horas

            asistencia=user_data.asistencia

            comprension=user_data.comprension

            razon=user_data.razon

            observaciones=user_data.observaciones

            calificacion=user_data.calificacion

            gusto=user_data.gusto

            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_e)
                elif action == 'evaluado':
                    return self.evaluado(asesoria)
                elif action == 'put':
                    return self.put(asesoria,horas,asistencia,comprension,razon,observaciones,calificacion,gusto)
                elif action == 'delete':
                    return self.delete(id_e)
                elif action == 'update':
                    return self.update(id_e, asesoria,horas,asistencia,comprension,razon,observaciones,calificacion,gusto)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
