from source import db


class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)
    image_file = db.Column(db.String(50), nullable=False,
                           default='default.png')
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    location = db.relationship('LocationModel')

    def __init__(self, username, password, first_name, last_name, location_id):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.location_id = location_id
