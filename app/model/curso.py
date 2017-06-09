from model import db

class Curso(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  id_jornada_curso = db.Column(db.Integer)
  letra = db.Column(db.String(50))
  grado = db.Column(db.String(50))
  def __init__(self, usuario_id):
    self.usuario_id = usuario_id
