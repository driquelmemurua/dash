from model import db

class JornadaCurso(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  id_jornada = db.Column(db.Integer)
  id_curso = db.Column(db.Integer)
  def __init__(self, usuario_id):
    self.usuario_id = usuario_id
