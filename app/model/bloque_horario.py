from model import db

class BloqueHorario(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  id_horario = db.Column(db.Integer)
  id_bloque = db.Column(db.Integer)
  id_curso = db.Column(db.Integer)
  id_asignatura_profesor = db.Column(db.Integer)
  def __init__(self, usuario_id):
    self.usuario_id = usuario_id
