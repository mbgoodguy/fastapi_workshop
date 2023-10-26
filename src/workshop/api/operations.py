from typing import List

from fastapi import APIRouter, Depends

from .. import tables
from ..database import Session, get_session
from ..models.operations import Operation

router = APIRouter(
    prefix='/operations'
)


# благодаря указания response_model pydantic автоматом преобразует список в модели pydantic и с помощью них на выходе получит JSON
@router.get('/', response_model=List[Operation])
def get_operations(session: Session = Depends(get_session)):
    operations = (session.query(tables.Operation).all())
    return operations
