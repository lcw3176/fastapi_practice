from models import Comment, Post
from datetime import datetime
from sqlalchemy.orm import Session


def find_by_page(db: Session, post_id: int, page: int, limit: int = 10):
    lst = db.query(Comment).filter(Comment.post_id == post_id).order_by(Comment.create_date.desc())

    total_size = lst.count()
    notice_list = lst.offset((page - 1) * limit).limit(limit).all()

    return {"total_page": total_size // limit + 1, "comment_list": notice_list}

def save(db: Session, post_id: int, writer: str, content: str, password: str):
    post = db.query(Post).filter(Post.id == post_id).first()
    
    if not post:
        return False
    
    comment = Comment(post_id=post_id, writer=writer, content=content, password=password, create_date=datetime.now())
    
    post.commentCount += 1
    db.add(comment)
    db.commit()

    return True


def delete(db: Session, comment_id: int, password: str):    
    comment = db.query(Comment).filter(Comment.id == comment_id and Comment.password == password)
    post_id = comment.first().post_id
    
    post = db.query(Post).filter(Post.id == post_id).first()
    post.commentCount -= 1

    comment.delete()
    db.commit()

    return True