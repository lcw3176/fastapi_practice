from fastapi import APIRouter, Depends, Response, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from domain.community.comment import service, scheme


router = APIRouter()


@router.get("/comment")
def get_list(post_id: int, page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    if page <= 0 or post_id <= 0:
        raise HTTPException(status_code=400, detail="잘못된 페이지 요청입니다")
    
    lists = service.find_by_page(db=db, post_id=post_id, page=page, limit=limit)
    
    return lists 


@router.post("/comment/register")
def register(request: scheme.CommentRegisterRequest, db: Session = Depends(get_db)):
    success = service.save(db=db, post_id=request.postId, writer=request.writer, content=request.content, password=request.password)

    if not success:
        raise HTTPException(status_code=400, detail="댓글 작성에 실패했습니다")

    return Response(status_code=200)


@router.get("/comment/delete/{comment_id}")
def get_list(comment_id: int, password: str, db: Session = Depends(get_db)):
    if comment_id <= 0:
        raise HTTPException(status_code=400, detail="잘못된 댓글 아이디 값입니다")
    
    success = service.delete(db=db, comment_id=comment_id, password=password)
    
    if not success:
        raise HTTPException(status_code=400, detail="댓글 삭제에 실패했습니다")
    
    return Response(status_code=200) 
