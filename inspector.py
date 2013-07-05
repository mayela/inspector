import pymongo
from bottle import get, post, request, route, run, template


def checkLogin(name,passwd):
    '''
        Documentar una funcion
        Esta funcion checara si el usuario y la contrasena son correctas 

        Args:
            name(str):Es el nombre del usuario
            password(str):Es el password correspondiente al nombre de usuario

        Returns:
            boolean:Si 
    '''
    Mongo=pymongo.MongoClient("localhost",27017)
    inspector=Mongo.inspector
    usuarios=inspector["usuarios"]

#    {"nombre":nombre,"edad":no,"email":algo@...,"pswd":md5()#}

    
    bus=usuarios.find_one({"nombre":name})
    print type(bus)
    print bus
    if name==bus["nombre"] and passwd==bus["password"]:
        return True
   
    return False

@route('/')

@get('/login')
def loginform():
    return template("login.tpl")
@post('/login')
def loginSubmit():
    name = request.forms.get('name')
    password = request.forms.get('password')
    if checkLogin(name,password):
        return '<h1> Bienvenido </h1>'
    else:
        return '<h1> Abrete, estas en mi barrio </h1>'

run(host = 'localhost', port=8080)
