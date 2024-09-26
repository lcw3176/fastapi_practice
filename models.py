from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from database import Base


class Notice(Base):
    __tablename__ = "notice"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    noticeType = Column(String, nullable=False)
    content = Column(String, nullable=False)
    create_date = Column(DateTime, nullable=False)


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True)
    writer = Column(String, nullable=False)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    password = Column(String, nullable=False)
    commentCount = Column(Integer, nullable=False)
    deleted = Column(Boolean)
    create_date = Column(DateTime, nullable=False)


class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True)
    writer = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    password = Column(String, nullable=False)
    deleted = Column(Boolean)
    create_date = Column(DateTime, nullable=False)
    post_id = Column(Integer, nullable=False)