from models import Notice
from datetime import datetime

from sqlalchemy.orm import Session


def find_by_page(db: Session, page: int, limit: int = 10):
    lst = db.query(Notice).order_by(Notice.create_date.desc())

    total_size = lst.count()
    notice_list = lst.offset((page - 1) * limit).limit(limit).all()

    return {"total_page": total_size // limit + 1, "notice_list": notice_list}


def find_by_id(db: Session, id: int):
    notice = db.query(Notice).filter(Notice.id == id).first()

    return notice


def save(db: Session, notice_type: str, title: str, content: str):
    notice = Notice(notice_type=notice_type, title=title, content=content, create_date=datetime.now())
    
    db.add(notice)
    db.commit()

    return True



def modify(db: Session, id: int,  notice_type: str, title: str, content: str):
    notice = db.query(Notice).filter(Notice.id == id).first()
    
    if notice == None:
        return False
    
    notice.notice_type = notice_type
    notice.title = title
    notice.content = content

    db.commit()    

    return True

def delete(db: Session, id: int):
    notice = db.query(Notice).filter(Notice.id == id)

    notice.delete()
    db.commit()

    return True


    # UPDATE("업데이트"),
    # FIX("오류수정"),
    # RESERVED_CHECK("점검예정")