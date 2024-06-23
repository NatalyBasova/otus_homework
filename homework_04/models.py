"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os


from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)


from sqlalchemy.orm import (
    DeclarativeBase,
    declared_attr,
)


from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    String,
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import text

# from sqlalchemy.orm import relationship


PG_CONN_URI = (
    os.environ.get("SQLALCHEMY_PG_CONN_URI")
    or "postgresql+asyncpg://postgres:password@localhost/postgres"
)


Session = None


async_engine = create_async_engine(url=PG_CONN_URI, echo=True)
Base = declarative_base()
async_session = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    autocommit=False,
    expire_on_commit=False,
)


async def init_models():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self) -> str:
        fields = self.__dict__.copy()
        fields.pop("_sa_instance_state")
        return str(fields)


class User(Base):

    name = Column(String)
    username = Column(String(32), nullable=False, unique=True)
    email = Column(String, nullable=True, unique=True)

    def __init__(self, iterable=(), **kwargs):
        self.__dict__.update(iterable, **kwargs)


# user = relationship("User", backref="Posts")


# class Post(Base):

#     user_id = Column(
#         Integer,
#         ForeignKey("users.id"),
#         unique=False,
#         nullable=False,
#     )
#     title = Column(
#         String(80),
#         nullable=False,
#         default="",
#         server_default="",
#     )
#     body = Column(Text, default="", server_default="")

#     post = relationship("Post", backref="User")

#     def __repr__(self):
#         return str(self)
