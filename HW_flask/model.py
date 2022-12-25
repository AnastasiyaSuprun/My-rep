from settings import db
from sqlalchemy import func


class Visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    email = db.Column(db.String(50), nullable=False, unique=True)
    create_at = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now(),
    )

    def __repr__(self):
        return f' Visitor {self.firstname} {self.lastname}'
