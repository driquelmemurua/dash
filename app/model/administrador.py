from model import db

class Administrador(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  usuario_id = db.Column(db.Integer, ForeignKey("usuario.id"), nullable=False)

  def __init__(self, usuario_id):
    self.usuario_id = usuario_id