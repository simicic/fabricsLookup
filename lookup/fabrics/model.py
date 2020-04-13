from lookup.extensions import db


class Fabric(db.Model):
    __tablename__ = "fabric"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.Text)
    href = db.Column(db.String(200))

    def __init__(self, name, description, href):
        self.name = name
        self.description = description
        self.href = href
