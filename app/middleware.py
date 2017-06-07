from flask import session

class administratorSession(object):

  def __init__(self, app):
    self.app = app 

  def __call__(self, environ, start_response):
    if not (session['name']):
      print "I'm in middleware"
    else:
      print "fucc"
    return self.app(environ, start_response)