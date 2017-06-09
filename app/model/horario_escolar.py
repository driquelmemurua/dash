from model import db

class HorarioEscolar(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  publicado = db.Column(db.Boolean)
  def __init__(self, usuario_id):
    self.usuario_id = usuario_id
