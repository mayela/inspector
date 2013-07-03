from bottle import get, post, request, route, run, template

@route('/')

@get('/login')
def loginform():
    return '''<form method="POST"
               action="/login">
              <input type="text"
                     name="name"/>
              <input type="password"
                     name="password"/>
              <input type="submit"/> 
              </form>''' 

@post('/login')
def loginSubmit():
    name = request.form.get('name')
    password = request.form.get('password')
    if checkLogin(name,password):
        return '<h1> Bienvenido </h1>'
    else:
        return '<h1> Abrete, estas en mi barrio </h1>'

run(host = 'localhost', port=8080)
