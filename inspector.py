from bottle import get, post, request, route, run, template

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
