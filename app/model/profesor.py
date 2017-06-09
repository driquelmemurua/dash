from model import db

class Profesor(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  usuario_id = db.Column(db.Integer, ForeignKey("usuario.id"), nullable=False)
  id_jornada_profesor = db.Column(db.Integer)
  def __init__(self, usuario_id):
    self.usuario_id = usuario_id