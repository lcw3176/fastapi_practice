from fastapi import HTTPException
from models import Comment, Post
from datetime import datetime
from sqlalchemy.orm import Session


def find_by_page(db: Session, post_id: int, page: int, limit: int = 10):
    if page <= 0:
        raise HTTPException(status_code=400, detail="잘못된 페이지 요청입니다")
    
    if post_id <= 0:
        raise HTTPException(status_code=400, detail="잘못된 게시글 아이디 값입니다")
    
    lst = db.query(Comment).filter(Comment.post_id == post_id).order_by(Comment.create_date.desc())

    total_size = lst.count()
    notice_list = lst.offset((page - 1) * limit).limit(limit).all()

    total_page = total_size // limit + 1

    if total_size % limit == 0:
        total_page = total_size // limit
    
    return {"total_page": total_page, "comment_list": notice_list}


def save(db: Session, post_id: int, writer: str, content: str, password: str):
    post = db.query(Post).filter(Post.id == post_id).first()
    
    if not post:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다")
    
    comment = Comment(post_id=post_id, writer=writer, content=content, password=password, create_date=datetime.now())
    post.commentCount += 1

    db.add(comment)
    db.commit()


def delete(db: Session, comment_id: int, password: str):  

    if comment_id <= 0:
        raise HTTPException(status_code=400, detail="잘못된 댓글 아이디 값입니다")
      
    comment = db.query(Comment).filter(Comment.id == comment_id, Comment.password == password).first()

    if not comment:
        raise HTTPException(status_code=404, detail="댓글을 찾을 수 없습니다")

    post_id = comment.post_id
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다")

    post.commentCount -= 1

    db.delete(comment)
    db.commit()