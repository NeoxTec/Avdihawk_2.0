import web
import config as config
import json


class Api_users:
    def get(self, user):
        try:
            # http://0.0.0.0:8080/api_users?user_hash=12345&action=get
            if user is None:
                result = config.model.get_all_users()
                users_json = []
                for row in result:
                    tmp = dict(row)
                    users_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(users_json)
            else:
                # http://0.0.0.0:8080/api_users?user_hash=12345&action=get&user=1
                result = config.model.get_users(user)
                users_json = []
                users_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(users_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            users_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(users_json)
    
    def get_nombre(self,user):
        try:
            # http://0.0.0.0:8080/api_users?user_hash=12345&action=get_nombre&user=1717110611@utectulancingo.edu.mx
            result = config.model.get_nombre(user)
            users_json = []
            users_json.append(dict(result))
            web.header('Content-Type', 'application/json')
            return json.dumps(users_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            users_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(users_json)

# http://0.0.0.0:8080/api_users?user_hash=12345&action=put&user=correo&nombre=nombre&carrera=carrera&grado=grado&tipo=tipo

    def put(self,user,nombre,carrera,grado,tipo):
        try:
            config.model.insert_users(user,nombre,carrera,grado,tipo)
            users_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(users_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_users?user_hash=12345&action=update&user=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self,user,grado):
        try:
            config.model.edit_grado(user,grado)
            users_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(users_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            users_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(users_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            user=None,
            nombre=None,
            carrera=None,
            grado=None,
            tipo=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            user=user_data.user

            nombre=user_data.nombre

            carrera=user_data.carrera

            grado=user_data.grado

            tipo=user_data.tipo

            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(user)
                elif action == 'get_nombre':
                    return self.get_nombre(user)
                elif action == 'put':
                    return self.put(user,nombre,carrera,grado,tipo)
                elif action == 'update':
                    return self.update(user,grado)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
