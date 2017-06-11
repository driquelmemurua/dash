#------------------------------IMPORT------------------------------#
#-----------PACKAGES------------#
import sys
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
import ast
#-------------------------------#
#------------------------------------------------------------------#

#-------------------------------INIT-------------------------------#
#--------------ENV--------------#
env = open('.env', 'r')
env = ast.literal_eval(env.read())
#-------------------------------#

#------------FILES--------------#
sys.path.append(env['MODULES_PATH'])
from router import routes
from model import db
#-------------------------------#

#-------------FLASK-------------#
app = Flask(__name__)
app.secret_key = env['SESSION_SECRET']
#-------------------------------#

#-----------SQLALCHEMY----------#
app.config['SQLALCHEMY_DATABASE_URI'] = env['DATABASE_URI']
db = model.db
#-------------------------------#

#-------------ROUTES------------#
app.register_blueprint(routes)
#-------------------------------#

#------------------------------------------------------------------#

#-------------------------------MAIN-------------------------------#
def main():
  db.create_all()
  app.run(host=env['SERVER_HOST'], port=env['SERVER_PORT'])
#------------------------------------------------------------------#