import web
import config
import json


class Api_valoracion:
    def get(self, num_val):
        try:
            # http://0.0.0.0:8080/api_valoracion?user_hash=12345&action=get
            if num_val is None:
                result = config.model.get_all_valoracion()
                valoracion_json = []
                for row in result:
                    tmp = dict(row)
                    valoracion_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(valoracion_json)
            else:
                # http://0.0.0.0:8080/api_valoracion?user_hash=12345&action=get&num_val=1
                result = config.model.get_valoracion(int(num_val))
                valoracion_json = []
                valoracion_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(valoracion_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            valoracion_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(valoracion_json)

# http://0.0.0.0:8080/api_valoracion?user_hash=12345&action=put&num_val=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, valor,asesoria):
        try:
            config.model.insert_valoracion(valor,asesoria)
            valoracion_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(valoracion_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_valoracion?user_hash=12345&action=delete&num_val=1
    def delete(self, num_val):
        try:
            config.model.delete_valoracion(num_val)
            valoracion_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(valoracion_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_valoracion?user_hash=12345&action=update&num_val=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, num_val, valor,asesoria):
        try:
            config.model.edit_valoracion(num_val,valor,asesoria)
            valoracion_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(valoracion_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            valoracion_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(valoracion_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            num_val=None,
            valor=None,
            asesoria=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            num_val=user_data.num_val
            valor=user_data.valor
            asesoria=user_data.asesoria
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(num_val)
                elif action == 'put':
                    return self.put(valor,asesoria)
                elif action == 'delete':
                    return self.delete(num_val)
                elif action == 'update':
                    return self.update(num_val, valor,asesoria)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
