from models import Notice
from datetime import datetime
from fastapi import HTTPException
from sqlalchemy.orm import Session


def find_by_page(db: Session, page: int, limit: int = 10):
    if page <= 0:
        raise HTTPException(status_code=400, detail="잘못된 페이지 요청입니다")
    
    lst = db.query(Notice).order_by(Notice.create_date.desc())

    total_size = lst.count()
    notice_list = lst.offset((page - 1) * limit).limit(limit).all()
    total_page = total_size // limit + 1

    if total_size % limit == 0:
        total_page = total_size // limit
    

    return {"total_page": total_page, "notice_list": notice_list}


def find_by_id(db: Session, id: int):
    if id <= 0:
        raise HTTPException(status_code=400, detail="잘못된 id 값입니다")
    
    notice = db.query(Notice).filter(Notice.id == id).first()

    if not notice:
        raise HTTPException(status_code=404, detail="공지사항을 찾을 수 없습니다")
    
    return notice


def save(db: Session, notice_type: str, title: str, content: str):
    notice = Notice(notice_type=notice_type, title=title, content=content, create_date=datetime.now())
    
    db.add(notice)
    db.commit()



def modify(db: Session, id: int,  notice_type: str, title: str, content: str):
    notice = db.query(Notice).filter(Notice.id == id).first()
    
    if not notice:
        raise HTTPException(status_code=404, detail="공지사항을 찾을 수 없습니다")
    
    notice.notice_type = notice_type
    notice.title = title
    notice.content = content

    db.commit()    

def delete(db: Session, id: int):
    notice = db.query(Notice).filter(Notice.id == id).first()

    if not notice:
        raise HTTPException(status_code=404, detail="공지사항을 찾을 수 없습니다")
    
    
    db.delete(notice)
    db.commit()


    # UPDATE("업데이트"),
    # FIX("오류수정"),
    # RESERVED_CHECK("점검예정")