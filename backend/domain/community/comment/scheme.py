from pydantic import BaseModel, field_validator

class CommentRegisterRequest(BaseModel):
    postId: int
    writer: str
    content: str
    password: str


    @field_validator("postId","writer", "content", "password")
    @classmethod
    def check(cls, v):
        if not str(v).strip():
            raise ValueError("공백 입력은 허용되지 않습니다.")
        return v
