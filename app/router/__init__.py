from flask import Blueprint, render_template, abort, redirect, url_for, request, Response, session
from jinja2 import TemplateNotFound
from model import usuario
from model.profesor import Profesor
from model.administrador import Administrador

routes = Blueprint('routes', __name__, template_folder='templates')

def verificar_usuario(username, password):
  usuario_login = usuario.Usuario.query.filter_by(rut=username).first()
  if usuario_login is None:
    return False
  if usuario.check_password(usuario_login.password, password):
    profesor_check = Profesor.query.filter_by(usuario_id=usuario_login.id).first()
    administrador_check = Administrador.query.filter_by(usuario_id=usuario_login.id).first()
    if profesor_check is not None:
      session['usuario'] = 'profesor'
      return True
    elif administrador_check is not None:
      session['usuario'] = 'administrador'
      return True
  return False


@routes.route('/login', methods=['POST', 'GET'])
def login():
  if request.method == 'POST':
    if not verificar_usuario(request.form['nombre'], request.form['password']):
      return redirect(url_for('routes.login'))
    if session['usuario'] is 'profesor':
      return redirect(url_for('routes.profesor'))
    elif session['usuario'] is 'administrador':
      return redirect(url_for('routes.administrador'))
  else:
    return render_template('login.html')

@routes.route('/logout')
def logout():
  session['usuario'] = None
  return redirect(url_for('routes.login'))

@routes.route('/administrador', defaults={'page': 'horarios'})
@routes.route('/administrador/<page>')
def administrador(page):
  try:
    if session['usuario'] != 'administrador':
  	  return redirect(url_for('routes.logout'))
    return render_template('%s-administrador.html' % page)
  except TemplateNotFound:
    abort(404)

@routes.route('/', defaults={'page': 'horario'})
@routes.route('/<page>')
def profesor(page):
  try:
    if session['usuario'] != 'profesor':
  	  return redirect(url_for('routes.logout'))
    return render_template('%s-profesor.html' % page)
  except TemplateNotFound:
    abort(404)
