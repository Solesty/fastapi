from blog.oauth2 import get_current_user
from typing import List

from fastapi import APIRouter
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from starlette import status
from blog import database


from .. import models, schemas
from ..repository import blog as blog_repo

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"],
)


@router.get("/", response_model=List[schemas.ShowBlog])
def all(
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    """
    Fetches all blog posts.
    """

    # We need a repo because the only function of the router is
    # to redirect the request to the right function to do the
    # right thing.

    return blog_repo.get_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(
    request: schemas.Blog,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    return blog_repo.create(db, request)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(
    id,
    request: schemas.Blog,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(get_current_user),
):

    return blog_repo.update(id, request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(
    id,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    """
    Deletes a single blog post.
    """
    return blog_repo.destroy(id, db)


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ShowBlog,
    tags=["Blogs"],
)
def show(
    id,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    """
    Shows a single blog post.
    """
    return blog_repo.show(id, db)
