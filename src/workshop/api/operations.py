from typing import List

from fastapi import APIRouter

from .. import tables
from ..database import Session
from ..models.operations import Operation

router = APIRouter(
    prefix='/operations'
)


# благодаря указания response_model pydantic автоматом преобразует список в модели pydantic и с помощью них на выходе получит JSON
@router.get('/', response_model=List[Operation])
def get_operations():
    # var 1 for
    session = Session()
    operations = (session.query(tables.Operation).all())
    return operations
