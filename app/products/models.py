from functools import partial

from sqlalchemy import Column

from .. import db

NotNullColumn = partial(Column, nullable=False)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    price = NotNullColumn(db.Numeric(10, 2))
    stock = NotNullColumn(db.Integer)
    description = db.Column(db.String(500))
    image = db.Column(db.String(100))
