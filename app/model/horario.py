from model import db

class Horario(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  id_horario_escolar = db.Column(db.Integer)
  def __init__(self, usuario_id):
    self.usuario_id = usuario_id
