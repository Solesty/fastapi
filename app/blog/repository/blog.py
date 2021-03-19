from http import HTTPStatus

from sqlalchemy.orm.session import Session
from starlette import status
from starlette.exceptions import HTTPException
from starlette.responses import Response

from blog import models, schemas


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(db: Session, request: schemas.Blog):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=2)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not available",
        )

    blog.update(
        {"title": request.title, "body": request.body},
    )
    db.commit()

    return "updated"


def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not available",
        )

    blog.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=HTTPStatus.NO_CONTENT.value)


def show(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not available",
        )
    return blog