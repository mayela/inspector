from bottle import request, route, run, template
from pymongo import MongoClient

@route('/')

@get('/login')
def loginform():
    return template("login.tpl")
@post('/login')
def loginSubmit():
    name = request.form.get('name')
    password = request.form.get('password')
    if checkLogin(name,password):
        return '<h1> Bienvenido </h1>'
    else:
        return '<h1> Abrete, estas en mi barrio </h1>'


@route('/consulta')

