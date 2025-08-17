from app.extensions import db
from app.models.post import SentPost

def post_already_sent(url):
    return db.session.query(SentPost).filter_by(url=url).first() is not None

def save_post(title, description, url, thumbnail):
    post = SentPost(title=title, description=description, url=url, thumbnail=thumbnail)
    if not post:
        return 'Error'
    
    db.session.add(post)
    db.session.commit()