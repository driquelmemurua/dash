from model import db

class JornadaProfesor(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  id_jornada = db.Column(db.Integer)
  id_profesor = db.Column(db.Integer)
  def __init__(self, usuario_id):
    self.usuario_id = usuario_id
