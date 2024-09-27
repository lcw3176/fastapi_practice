from fastapi import APIRouter, Depends, Response, HTTPException
from sqlalchemy.orm import Session
from domain.notice import scheme
from domain.notice import service
from database import get_db


router = APIRouter()


@router.get("/notice")
def get_list(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    if page <= 0:
        raise HTTPException(status_code=400, detail="잘못된 페이지 요청입니다")
    
    lists = service.find_by_page(db=db, page=page, limit=limit)
    
    return lists 


@router.get("/notice/{notice_id}")
def get_detail(notice_id: int, db: Session = Depends(get_db)):
    if notice_id <= 0:
        raise HTTPException(status_code=400, detail="잘못된 id 값입니다")
    
    notice = service.find_by_id(db=db, id=notice_id)
    
    if notice == None:
        raise HTTPException(status_code=400, detail="존재하지 않는 공지사항입니다")

    return notice 


@router.post("/notice/register")
def register(request: scheme.NoticeRegisterRequest, db: Session = Depends(get_db)):
    service.save(db=db, notice_type=request.notice_type, title=request.title, content=request.content)
    
    return Response(status_code=200, content="success")


@router.post("/notice/modify/{notice_id}")
def modify(notice_id: int, request: scheme.NoticeModifyRequest, db: Session = Depends(get_db)):
    success = service.modify(db=db, id=notice_id, notice_type=request.notice_type, title=request.title, content=request.content)
    
    if not success:
        raise HTTPException(status_code=400, detail="잘못된 id 값입니다")
    
    return Response(status_code=200, content="success")


@router.get("/notice/delete/{notice_id}")
def register(notice_id: int, db: Session = Depends(get_db)):
    service.delete(db=db, id=notice_id)

    return Response(status_code=200, content="success")