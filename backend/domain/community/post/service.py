from fastapi import HTTPException
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
    if page <= 0:
        raise HTTPException(status_code=400, detail="잘못된 게시글 요청입니다")
    
    lst = db.query(Post).order_by(Post.create_date.desc())

    total_size = lst.count()
    post_list = lst.offset((page - 1) * limit).limit(limit).all()

    for i in post_list:
        del i.password
        del i.content

    total_page = total_size // limit + 1

    if total_size % limit == 0:
        total_page = total_size // limit
    
    
    return {"total_page": total_page, "post_list": post_list }


def find_by_id(db: Session, id: int):
    if id <= 0:
        raise HTTPException(status_code=400, detail="잘못된 게시글 요청입니다")
    
    post = db.query(Post).filter(Post.id == id).first()

    return post


def delete(db: Session, id: int, password: str):
    post = db.query(Post).filter(Post.id == id, Post.password == password).first()
    comments = db.query(Comment).filter(Comment.post_id == post.id)
    
    comments.delete()

    db.delete(post)
    db.commit()
