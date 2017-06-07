from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

routes = Blueprint('routes', __name__, template_folder='templates')

@routes.route('/', defaults={'page': 'horarios'})
@routes.route('/<page>')
def show(page):
  try:
    return render_template('%s.html' % page)
  except TemplateNotFound:
    abort(404)