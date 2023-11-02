from typing import List

from fastapi import APIRouter, Depends
from ..models.operations import Operation, OperationKind
from ..services.operations import OperationService

router = APIRouter(
    prefix='/operations'
)


# благодаря указания response_model pydantic автоматом преобразует список в модели pydantic и с помощью них на выходе получит JSON
@router.get('/', response_model=List[Operation])
def get_operations(kind: OperationKind = None, service: OperationService = Depends()):
    return service.get_list(kind=kind)
