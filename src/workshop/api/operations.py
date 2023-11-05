from typing import List

from fastapi import APIRouter, Depends
from starlette.responses import Response

from ..models.operations import Operation, OperationKind, OperationCreate, OperationUpdate
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


@router.get('/{user_id}', response_model=Operation)
def get_operation_by_id(
        operation_id: int,
        service: OperationService = Depends()
):
    return service.get_operation(operation_id)


@router.put('/{operation_id}', response_model=Operation)
def update_operation_by_id(
        operation_id: int,
        operation_data: OperationUpdate,
        service: OperationService = Depends(),
):
    return service.update_operation(operation_id, operation_data)


@router.delete('/{operation_id}', response_model=Operation)
def delete_operation_by_id(
        operation_id: int,
        service: OperationService = Depends(),
):
    service.delete_operation(operation_id)
    return Response(status_code=204)
