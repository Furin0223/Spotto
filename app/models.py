from . import db

class Train(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_en = db.Column(db.String(100), nullable=False)
    name_jp = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text, nullable=False)
    image_filename = db.Column(db.String(100), nullable=True)
    region = db.Column(db.String(50), nullable=True)
    operator = db.Column(db.String(50), nullable=True)
    tags = db.Column(db.String(200), nullable=True)
