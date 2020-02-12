from .db import db


class Routes(db.Document):
    route_description = db.StringField()
    route_name = db.StringField(required=True, unique=True)
    route_picture = db.StringField()
    route_type = db.StringField()
    route_pubCount = db.IntField()

class Users(db.Document):
    username = db.StringField(required=True, unique=True)
    avatar = db.StringField()
    active_route = db.ListField(db.IntField())
    bio  = db.StringField()

class Test(db.Document):
    username = db.StringField(required=True, unique=True)
    avatar = db.StringField()
    active_route = db.ListField(db.IntField())
    bio  = db.StringField()


class Pubs(db.Document):
    pub_name = db.StringField(required=True)
    pub_description = db.StringField(required=True)
    pub_picture = db.StringField(required=True)
    pub_address = db.StringField(required=True)
    lat = db.FloatField(required=True)
    lng = db.FloatField(required=True)
    
# class UserRoutes(db.Document):