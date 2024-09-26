from models import Post
from datetime import datetime

from sqlalchemy.orm import Session




def save_post(db: Session, writer, title, content, password):
    post = Post(writer=writer, 
                title=title, 
                content=content, 
                password=password, 
                commentCount=0, 
                deleted=False, 
                create_date=datetime.now())
    
    db.add(post)
    db.commit()


def get_posts(db: Session):
    return db.query(Post).order_by(Post.create_date.desc()).all()