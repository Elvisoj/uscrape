from app.extensions import db
from datetime import datetime

class SentPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(250), nullable=False)
    thumbnail = db.Column(db.String(250))
    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.Text, nullable=False)
    sent_at = db.Column(db.DateTime, default=datetime.utcnow)