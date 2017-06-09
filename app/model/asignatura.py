from model import db

class Asignatura(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nombre = db.Column(db.String(50))
  grado = db.Column(db.String(50))
  def __init__(self, usuario_id):
    self.usuario_id = usuario_id
