from model import db

class Sugerencia(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  profesor_id = db.Column(db.Integer, ForeignKey("profesor.id"), nullable=False)
  titulo = db.Column(db.String(50), unique=True, nullable=False)
  contenido = db.Column(db.String(500), unique=True, nullable=False)
  estado = db.Column(db.String(50), unique=True, nullable=False)
  def __init__(self, usuario_id):
    self.usuario_id = usuario_id
