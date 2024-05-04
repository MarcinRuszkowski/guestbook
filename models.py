from config import db


class Entry(db.Model):
    __tablename__ = 'entries'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'content': self.content
        }