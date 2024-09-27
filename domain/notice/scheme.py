from pydantic import BaseModel, field_validator


class NoticeRegisterRequest(BaseModel):
    notice_type: str
    title: str
    content: str
    
    @field_validator("notice_type", "title", "content")
    @classmethod
    def check(cls, v):
        if not str(v).strip():
            raise ValueError("공백 입력은 허용되지 않습니다.")
        return v


class NoticeModifyRequest(BaseModel):
    notice_type: str
    title: str
    content: str
    
    @field_validator("notice_type", "title", "content")
    @classmethod
    def check(cls, v):
        if not str(v).strip():
            raise ValueError("공백 입력은 허용되지 않습니다.")
        return v