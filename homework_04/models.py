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


# from sqlalchemy.ext.asyncio import (
#     create_async_engine,
#     async_sessionmaker,
# )
# import config

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

# from sqlalchemy.orm import relationship


PG_CONN_URI = (
    os.environ.get("SQLALCHEMY_PG_CONN_URI")
    or "postgresql+asyncpg://postgres:password@localhost/postgres"
)

Base = None
Session = None

# async_engine = create_async_engine(
#     url=config.DB_URL,
#     echo=config.DB_ECHO,
# )
# async_session = async_sessionmaker(
#     bind=async_engine,
#     autocommit=False,
#     expire_on_commit=False,
# )


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
