from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from domain.notice import scheme
from domain.notice import service
from database import get_db

router = APIRouter()

@router.get("/notice")
def get_list(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    lists = service.find_by_page(db=db, page=page, limit=limit)
    
    return lists 


@router.get("/notice/{notice_id}")
def get_detail(notice_id: int, db: Session = Depends(get_db)):
    notice = service.find_by_id(db=db, id=notice_id)
    
    return notice 


@router.post("/notice/register")
def register(request: scheme.NoticeRegisterRequest, db: Session = Depends(get_db)):
    service.save(db=db, notice_type=request.notice_type, title=request.title, content=request.content)
    
    return Response(status_code=200, content="success")


@router.post("/notice/modify/{notice_id}")
def modify(notice_id: int, request: scheme.NoticeModifyRequest, db: Session = Depends(get_db)):
    service.modify(db=db, id=notice_id, notice_type=request.notice_type, title=request.title, content=request.content)

    return Response(status_code=200, content="success")


@router.get("/notice/delete/{notice_id}")
def register(notice_id: int, db: Session = Depends(get_db)):
    service.delete(db=db, id=notice_id)

    return Response(status_code=200, content="success")