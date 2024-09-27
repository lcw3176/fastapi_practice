from pydantic import BaseModel, field_validator


class PostRegisterRequest(BaseModel):
    writer: str
    title: str
    content: str
    password: str


    @field_validator("writer", "title", "content", "password")
    @classmethod
    def check(cls, v):
        value = str(v).strip()
        if not value or value == "":
            raise ValueError("공백 입력은 허용되지 않습니다.")
        return v
    