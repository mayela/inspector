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
    bus=usuarios.find_one({"nombre":name})
    if name==bus["nombre"] and passwd==bus["password"]:
        return True
    else:   
        return False

@get('/login')
def loginform():
    return template("login")

@post('/login')
def loginSubmit():
    name = request.forms.get('name')
    password = request.forms.get('password')
    if checkLogin(name,password):
        return '<h1> Bienvenido </h1>'
    else:
        return '<h1> El usuario y contrasena no coinciden </h1>'

run(host = 'localhost', port=8080,reloader=True)
