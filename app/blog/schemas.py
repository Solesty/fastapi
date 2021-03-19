from typing import List, Optional

from pydantic import BaseModel

# Request Schema
# -------------------------


class User(BaseModel):
    name: str
    email: str
    password: str


class BlogBase(BaseModel):
    """
    Schema to receive content from the client
    """

    title: str
    body: str


class Blog(BlogBase):
    class Config:
        orm_mode = True


class Login(BaseModel):
    email: str
    password: str


# Response Models
# -------------------------
"""
Is used to display the result of an API query.
A response that is similar to this. Think of it like
a simple serializer.
"""


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config:
        orm_mode = True


class ShowBlog(BaseModel):
    """
    Is used to display the result of an API query.
    A response that is similar to this. Think of it like
    a simple serializer.
    """

    title: str
    body: str

    # this will allow the response to have nested values.
    # will show the details of the creator
    creator: ShowUser

    class Config:
        orm_mode = True


# Token Schemas
# ---------------------------------
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
