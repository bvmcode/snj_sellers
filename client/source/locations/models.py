from source import db


class LocationModel(db.Model):
    __tablename__ = 'location'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    state = db.Column(db.String(20), nullable=False)
    zip_code = db.Column(db.String(50), nullable=False)
    users = db.relationship('UserModel', lazy='dynamic')

    def __init__(self, address, city, state, zip_code):
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
