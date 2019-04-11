import web
import config as config
import json


class Api_asesor:
    def get(self, id_as):
        try:
            # http://0.0.0.0:8080/api_asesor?user_hash=12345&action=get
            if id_as is None:
                result = config.model.get_all_asesor()
                asesor_json = []
                for row in result:
                    tmp = dict(row)
                    asesor_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(asesor_json)
            else:
                # http://0.0.0.0:8080/api_asesor?user_hash=12345&action=get&id_as=1
                result = config.model.select_id_as(int(id_as))
                asesor_json = []
                asesor_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(asesor_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            asesor_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(asesor_json)
    
    def get_correo(self, correo):
        try:
            # http://0.0.0.0:8080/api_asesor?user_hash=12345&action=get
            if correo is None:
                result = config.model.get_all_asesor()
                asesor_json = []
                for row in result:
                    tmp = dict(row)
                    asesor_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(asesor_json)
            else:
                # http://0.0.0.0:8080/api_asesor?user_hash=12345&action=get&id_as=1
                result = config.model.get_asesor(correo)
                asesor_json = []
                asesor_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(asesor_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            asesor_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(asesor_json)

# http://0.0.0.0:8080/api_asesor?user_hash=12345&action=put&id_as=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre,correo,carrera,horario,habilidades,grado):
        try:
            config.model.insert_asesor(nombre,correo,carrera,horario,habilidades,grado)
            asesor_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(asesor_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_asesor?user_hash=12345&action=delete&id_as=1
    def delete(self, id_as):
        try:
            config.model.delete_asesor(id_as)
            asesor_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(asesor_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_asesor?user_hash=12345&action=update&id_as=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self,id_as,validado):
        try:
            config.model.update_validacion(id_as,validado)
            asesor_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(asesor_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            asesor_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(asesor_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_as=None,
            nombre=None,
            correo=None,
            carrera=None,
            horario=None,
            habilidades=None,
            grado=None,
            validado=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_as=user_data.id_as

            nombre=user_data.nombre

            correo=user_data.correo

            carrera=user_data.carrera

            horario=user_data.horario

            habilidades=user_data.habilidades

            grado=user_data.grado

            validado=user_data.validado

            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_as)
                elif action == 'get_correo':
                    return self.get_correo(correo)
                elif action == 'put':
                    return self.put(nombre,correo,carrera,horario,habilidades,grado)
                elif action == 'delete':
                    return self.delete(id_as)
                elif action == 'update':
                    return self.update(id_as,validado)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
