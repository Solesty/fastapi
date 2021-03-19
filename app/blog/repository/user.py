from blog.hashing import Hash
from fastapi import HTTPException

from sqlalchemy.orm.session import Session
from starlette import status

from blog import models, schemas


def get(id: int, db: Session):

    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the id {id} not found",
        )

    return user


def create(request: schemas.User, db: Session):

    hased_passwrod = Hash.brcypt(request.password)

    new_user = models.User(
        name=request.name,
        email=request.email,
        password=hased_passwrod,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user