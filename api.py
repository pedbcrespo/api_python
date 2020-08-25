import json
from flask import Flask, request
from flask_restful import Resource, Api
import data_bd

app = Flask(__name__)
api = Api(app)


class User(Resource):
    def get(self):
        return data_bd.get_data('usuario')

    def post(self):
        data_local = json.loads(request.data)
        try:
            data_bd.post_data('usuario', data_local)
            return {"status": "sucesso", "info": data_local}
        except Exception:
            return {"status": "ERRO", "info": Exception.__class__}

class UserAlt(Resource):

    def get(self, id):
        list_bd = data_bd.get_data('usuario')
        try:
            return [elem for elem in list_bd if elem['id'] == id][0]
        except Exception:
            return f"ERRO {Exception.__name__}"

    def put(self, id):
        data_local = json.loads(request.data)
        try:
            data_bd.put_data('usuario', id, data_local)
            return {"status": "sucesso", "info": data_local}
        except Exception:
            return {"status": "ERRO", "info": Exception.__class__}

    def delete(self, id):
        try:
            data_bd.delete_data('usuario', id)
            return {"status": "sucesso", "info": "dado deletado"}
        except Exception:
            return {"status": "ERRO", "info": Exception.__class__}


class Lotes(Resource):
    def get(self):
        return data_bd.get_data('lotes')

    def post(self):
        data_local = json.loads(request.data)
        try:
            data_bd.post_data('lotes', data_local)
            return {"status": "sucesso", "info": data_local}
        except Exception:
            return {"status": "ERRO", "info": Exception.__class__}

class LotesAlt(Resource):
    def get(self, id):
        list_bd = data_bd.get_data('lotes')
        try:
            return [elem for elem in list_bd if elem['id'] == id][0]
        except Exception:
            return f"ERRO {Exception.__name__}"

    def put(self, id):
        data_local = json.loads(request.data)
        try:
            data_bd.put_data('lotes', id, data_local)
            return {"status": "sucesso", "info": data_local}
        except Exception:
            return {"status": "ERRO", "info": Exception.__class__}

    def delete(self, id):
        try:
            data_bd.delete_data('lotes', id)
            return {"status": "sucesso", "info": "dado deletado"}
        except Exception:
            return {"status": "ERRO", "info": Exception.__class__}


api.add_resource(User, '/users/')
api.add_resource(UserAlt, '/users/<int:id>/')
api.add_resource(Lotes, '/lotes/')
api.add_resource(LotesAlt, '/lotes/<int:id>/')

if __name__ == '__main__':
    app.run(debug=True)
