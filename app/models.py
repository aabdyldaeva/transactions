from . import db


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer)
    status = db.Column(db.String)
    unit = db.Column(db.String)
    comment = db.Column(db.String)

    def __repr__(self):
        return self.name
