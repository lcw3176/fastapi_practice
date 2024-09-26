from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from domain.community import scheme
from domain.community import service

from database import get_db

router = APIRouter()

@router.get("/list")
def post_list(db: Session = Depends(get_db)):
    lists = service.get_posts(db=db)
    
    return lists 

@router.get("/register")
def post_list(request: scheme.PostRegisterRequest = Depends(), db: Session = Depends(get_db)):
    service.save_post(db=db, writer=request.writer, title=request.title, content=request.content, password=request.password)

    return Response(status_code=200)
