from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from domain.community.post import scheme, service
from database import get_db

router = APIRouter()

@router.get("/post")
def get_list(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    lists = service.find_by_page(db=db, page=page, limit=limit)

    return lists


@router.get("/post/{post_id}")
def get_detail(post_id: int, db: Session = Depends(get_db)):
    post = service.find_by_id(db=db, id=post_id)
    
    return post


@router.post("/post/register")
def register(request: scheme.PostRegisterRequest, db: Session = Depends(get_db)):
    service.save(db=db, writer=request.writer, title=request.title, content=request.content, password=request.password)

    return Response(status_code=200)


@router.get("/post/delete/{post_id}")
def delete(post_id: int, password: str, db: Session = Depends(get_db)):
    service.delete(db=db, id=post_id, password=password)

    return Response(status_code=200)