from typing import List

from fastapi import APIRouter, Depends

from .. import tables
from ..database import Session, get_session
from ..models.operations import Operation, OperationKind, OperationCreate
from ..services.operations import OperationService

router = APIRouter(
    prefix='/operations'
)


# благодаря указания response_model pydantic автоматом преобразует список в модели pydantic и с помощью них на выходе получит JSON
@router.get('/', response_model=List[Operation])
def get_operations(kind: OperationKind = None, service: OperationService = Depends()):
    return service.get_operations_list(kind=kind)


@router.post('/', response_model=OperationCreate)
def create_operations(
        operation_data: OperationCreate,
        service: OperationService = Depends()
):
    return service.add_operations(operation_data)
