#-----------------------------PACKAGES-----------------------------#
import sys
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
import ast
#------------------------------------------------------------------#

#-------------------------------INIT-------------------------------#
#--------------ENV--------------#
env = open('.env', 'r')
env = ast.literal_eval(env.read())
#-------------------------------#

#-------------FILES-------------#
sys.path.append(env['MODULES_PATH'])
from router import routes
from model import *
from seed import seed
#-------------------------------#

#------------------------------------------------------------------#
#-------------------------------MAIN-------------------------------#
def main():

  app = Flask(__name__)
  app.config['DEBUG'] = env['DEBUG']
  app.secret_key = env['SESSION_SECRET']
  app.config['SQLALCHEMY_DATABASE_URI'] = env['DATABASE_URI']
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  app.register_blueprint(routes)
  db.init_app(app)
  with app.app_context():
    db.create_all()
    if env['SEED']:
      db.reflect()
      db.drop_all()
      db.create_all()
      seed(db)
  app.run(host=env['SERVER_HOST'], port=env['SERVER_PORT'])
#------------------------------------------------------------------#