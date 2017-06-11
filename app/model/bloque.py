from model import db

class Bloque(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  hora_inicio = db.Column(db.Date, unique=True, nullable=False)
  hora_termino = db.Column(db.Date, unique=True, nullable=False)
  dia = db.Column(db.String(10), unique=True, nullable=False)
  
  def __init__(self, hora_inicio, hora_termino, dia):
    self.hora_inicio = hora_inicio
    self.hora_termino = hora_termino
    self.dia = dia