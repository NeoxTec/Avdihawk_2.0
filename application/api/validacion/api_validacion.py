import web
import config
import json


class Api_validacion:
    def get(self, num_val):
        try:
            # http://0.0.0.0:8080/api_validacion?user_hash=12345&action=get
            if num_val is None:
                result = config.model.get_all_validacion()
                validacion_json = []
                for row in result:
                    tmp = dict(row)
                    validacion_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(validacion_json)
            else:
                # http://0.0.0.0:8080/api_validacion?user_hash=12345&action=get&num_val=1
                result = config.model.get_validacion(int(num_val))
                validacion_json = []
                validacion_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(validacion_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            validacion_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(validacion_json)

# http://0.0.0.0:8080/api_validacion?user_hash=12345&action=put&num_val=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, tipo,asesor,profesor):
        try:
            config.model.insert_validacion(tipo,asesor,profesor)
            validacion_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(validacion_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_validacion?user_hash=12345&action=delete&num_val=1
    def delete(self, num_val):
        try:
            config.model.delete_validacion(num_val)
            validacion_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(validacion_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_validacion?user_hash=12345&action=update&num_val=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, num_val, tipo,asesor,profesor):
        try:
            config.model.edit_validacion(num_val,tipo,asesor,profesor)
            validacion_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(validacion_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            validacion_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(validacion_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            num_val=None,
            tipo=None,
            asesor=None,
            profesor=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            num_val=user_data.num_val
            tipo=user_data.tipo
            asesor=user_data.asesor
            profesor=user_data.profesor
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(num_val)
                elif action == 'put':
                    return self.put(tipo,asesor,profesor)
                elif action == 'delete':
                    return self.delete(num_val)
                elif action == 'update':
                    return self.update(num_val, tipo,asesor,profesor)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
