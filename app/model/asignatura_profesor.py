from model import db

class AsignaturaProfesor(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  id_asignatura = db.Column(db.Integer)
  id_profesor = db.Column(db.Integer)
  def __init__(self, usuario_id):
    self.usuario_id = usuario_id
