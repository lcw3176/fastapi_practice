from models import Post, Comment
from datetime import datetime
from sqlalchemy.orm import Session


def save(db: Session, writer: str, title: str, content: str, password: str):
    post = Post(writer=writer, 
                title=title, 
                content=content, 
                password=password, 
                commentCount=0, 
                create_date=datetime.now())
    
    db.add(post)
    db.commit()

    return True


def find_by_page(db: Session, page: int, limit: int):
    lst = db.query(Post).order_by(Post.create_date.desc())

    total_size = lst.count()
    post_list = lst.offset((page - 1) * limit).limit(limit).all()

    for i in post_list:
        del i.password
        del i.content
    
    return {"total_page": total_size // limit + 1, "post_list": post_list }


def find_by_id(db: Session, id: int):
    post = db.query(Post).filter(Post.id == id).first()

    return post


def delete(db: Session, id: int, password: str):
    post = db.query(Post).filter(Post.id == id, Post.password == password).first()
    comments = db.query(Comment).filter(Comment.post_id == post.id)
    
    comments.delete()
    db.delete(post)
    db.commit()

    return True
