from bottle import get, post, request, route, run, template

def checkLogin(name,password):
    if name=='admin' and password=='admin':
        return True
    else:
        return False

@route('/')
def hola():
    return "hola mundo"

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
        return '<h1> Abrete, estas en mi barrio </h1>'

run(host = 'localhost', port=8080, reloader=True)
