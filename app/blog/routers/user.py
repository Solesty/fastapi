from blog.oauth2 import get_current_user
from fastapi import APIRouter
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from blog import database


from blog import schemas
from blog.repository import user as user_repo

router = APIRouter(prefix="/user", tags=["Users"])


@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(
    id: int,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    return user_repo.get(id, db)


@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    """
    Creates the user for the application.
    """
    return user_repo.create(request, db)