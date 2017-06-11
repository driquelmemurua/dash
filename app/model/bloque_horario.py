from model import db

class BloqueHorario(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  horario_id = db.Column(db.Integer, ForeignKey("horario.id"), nullable=False)
  bloque_id = db.Column(db.Integer, ForeignKey("bloque.id"), nullable=False)
  curso_id = db.Column(db.Integer, ForeignKey("curso.id"), nullable=False)
  asignatura_profesor_id = db.Column(db.Integer, ForeignKey("asignatura_profesor.id"), nullable=False)
  
  def __init__(self, horario_id, bloque_id, curso_id, asignatura_profesor_id):
    self.horario_id = horario_id
    self.bloque_id = bloque_id
    self.curso_id = curso_id
    self.asignatura_profesor_id = asignatura_profesor_id			