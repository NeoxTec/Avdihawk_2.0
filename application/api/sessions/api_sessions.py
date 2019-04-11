import web
import config
import json


class Api_sessions:
    def get(self, session_id):
        try:
            # http://0.0.0.0:8080/api_sessions?user_hash=12345&action=get
            if session_id is None:
                result = config.model.get_all_sessions()
                sessions_json = []
                for row in result:
                    tmp = dict(row)
                    sessions_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(sessions_json)
            else:
                # http://0.0.0.0:8080/api_sessions?user_hash=12345&action=get&session_id=1
                result = config.model.get_sessions(int(session_id))
                sessions_json = []
                sessions_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(sessions_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            sessions_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(sessions_json)

# http://0.0.0.0:8080/api_sessions?user_hash=12345&action=put&session_id=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, atime,data):
        try:
            config.model.insert_sessions(atime,data)
            sessions_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(sessions_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_sessions?user_hash=12345&action=delete&session_id=1
    def delete(self, session_id):
        try:
            config.model.delete_sessions(session_id)
            sessions_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(sessions_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_sessions?user_hash=12345&action=update&session_id=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, session_id, atime,data):
        try:
            config.model.edit_sessions(session_id,atime,data)
            sessions_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(sessions_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            sessions_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(sessions_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            session_id=None,
            atime=None,
            data=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            session_id=user_data.session_id
            atime=user_data.atime
            data=user_data.data
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(session_id)
                elif action == 'put':
                    return self.put(atime,data)
                elif action == 'delete':
                    return self.delete(session_id)
                elif action == 'update':
                    return self.update(session_id, atime,data)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
