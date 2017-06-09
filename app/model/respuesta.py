from model import db

class Respuesta(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  sugerencia_id = db.Column(db.Integer, ForeignKey("sugerencia.id"), nullable=False)
  contenido = db.Column(db.String(500), unique=True, nullable=False)
  def __init__(self, usuario_id):
    self.usuario_id = usuario_id
