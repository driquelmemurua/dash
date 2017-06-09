from model import db

class Administrator(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column id = db.Column(db.Integer, ForeignKey("usuario.id")),

  def __init__(self, user_id):
    self.user_id = user_id