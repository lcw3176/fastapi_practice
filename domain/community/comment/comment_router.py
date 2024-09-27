from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from domain.community.comment import service, scheme
from database import get_db

router = APIRouter()

@router.get("/comment")
def get_list(post_id: int, page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    lists = service.find_by_page(db=db, post_id=post_id, page=page, limit=limit)
    
    return lists 


@router.post("/comment/register")
def register(request: scheme.CommentRegisterRequest, db: Session = Depends(get_db)):
    service.save(db=db, post_id=request.postId, writer=request.writer, content=request.content, password=request.password)

    return Response(status_code=200)


@router.get("/comment/delete/{comment_id}")
def get_list(comment_id: int, password: str, db: Session = Depends(get_db)):
    service.delete(db=db, comment_id=comment_id, password=password)

    return Response(status_code=200) 
