from flask import Response, request
from database.models import Pubs
from flask_restful import Resource

class PubsApi(Resource):
    def get(self):
        pubs = Pubs.objects().to_json()
        return Response(pubs, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        pub =  Pubs(**body).save()
        id = movie.id
        return {'id': str(id)}, 200
        
class PubApi(Resource):
    def put(self, id):
        body = request.get_json()
        Pubs.objects.get(id=id).update(**body)
        return '', 200
    
    def delete(self, id):
        pub = Pubs.objects.get(id=id).delete()
        return '', 200

    def get(self, id):
        pubs = Pubs.objects.get(id=id).to_json()
        return Response(pubs, mimetype="application/json", status=200)