from api import db
from marshmallow import fields, Schema

class UserModel(db.Model):

  #Table name
  __tablename__ = 'Users'

  id = db.Column(db.Integer, primary_key=True)
  user_name = db.Column(db.String(128), nullable=False)
  address = db.Column(db.String(128), nullable=False)

  #class constructor
  def __init__(self, data):
    self.id = data.get('id')
    self.user_name = data.get('user_name')
    self.address = data.get('address')
    
  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  @staticmethod
  def get_all_users():
    return UserModel.query.all()

  @staticmethod
  def get_user_by_id(id):
    return UserModel.query.filter_by(id=id).first()

  def __repr(self):
      return '<id {}>'.format(self.id)


class UserSchema(Schema):
  id = fields.Int(required=True)
  user_name = fields.Str(required=True)
  address = fields.Str(required=True)