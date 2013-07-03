from bottle import request, route, run, template
from pymongo import MongoClient

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

@route('/consulta')

