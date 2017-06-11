from functools import wraps
from flask import request, Response
from model import usuario, profesor, administrador

def verificar_profesor(username, password):
  """This function is called to check if a username /
  password combination is valid.
  """
  usuario_login = usuario.Usuario.query.filter_by(rut=username).first()
  if usuario_login is None:
    return False
  if usuario.check_password(usuario_login.password, password):
    if profesor.Profesor.query.filter_by(usuario_id=usuario_login.id) is not None:
        return True
  return False

def verificar_administrador(username, password):
  """This function is called to check if a username /
  password combination is valid.
  """
  usuario_login = usuario.Usuario.query.filter_by(rut=username).first()
  if usuario_login is None:
    return False
  if usuario.check_password(usuario_login.password, password):
    if administrador.Administrador.query.filter_by(usuario_id=usuario_login.id) is not None:
      return True
  return False

def authenticate():
  """Sends a 401 response that enables basic auth"""
  return Response(
  'Error en el login.\n', 401,
  {'WWW-Authenticate': 'Basic realm="Login Required"'})

def auth_profesor(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    auth = request.authorization
    if not auth or not verificar_profesor(auth.username, auth.password):
      return authenticate()
    return f(*args, **kwargs)
  return decorated

def auth_administrador(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    auth = request.authorization
    if not auth or not verificar_administrador(auth.username, auth.password):
      return authenticate()
    return f(*args, **kwargs)
  return decorated