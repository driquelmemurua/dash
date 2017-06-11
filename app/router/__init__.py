from middleware import auth_profesor, auth_administrador
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

routes = Blueprint('routes', __name__, template_folder='templates')

@routes.route('/', defaults={'page': 'horario'})
@routes.route('/<page>')
@auth_profesor
def profesor(page):
  try:
    return render_template('%s-profesor.html' % page)
  except TemplateNotFound:
    abort(404)

@routes.route('/administrador', defaults={'page': 'horarios'})
@routes.route('/administrador/<page>')
@auth_administrador
def administrador(page):
  try:
    return render_template('%s-administrador.html' % page)
  except TemplateNotFound:
    abort(404)