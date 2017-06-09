from model import db

class Jornada(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  def __init__(self, usuario_id):
    self.usuario_id = usuario_id
