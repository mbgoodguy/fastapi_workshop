from typing import List

from fastapi import Depends, HTTPException
from starlette import status

from workshop import tables
from workshop.database import get_session, Session
from workshop.models.operations import OperationKind, OperationCreate, OperationUpdate


class OperationService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, operation_id: int) -> tables.Operation:
        operation = (
            self.session
            .query(tables.Operation)
            .filter_by(id=operation_id)
            .first()
        )
        if not operation:
            raise HTTPException(status_code=404, detail=f'No operation with id {operation_id}')
        return operation

    def get_operations_list(self, kind: OperationKind) -> List[tables.Operation]:
        query = self.session.query(tables.Operation)
        if kind:
            query = query.filter_by(kind=kind)
        operations = query.all()
        return operations

    def add_operations(self, operation_data: OperationCreate) -> tables.Operation:
        operation = tables.Operation(**operation_data.model_dump())
        self.session.add(operation)
        self.session.commit()
        return operation

    def get_operation(self, operation_id: int) -> tables.Operation:
        return self._get(operation_id)

    def update_operation(self, operation_id: int, operation_data: OperationUpdate) -> tables.Operation:
        operation = self._get(operation_id)

        for field, value in operation_data:
            setattr(operation, field, value)
        self.session.commit()
        return operation

    def delete_operation(self, operation_id: int):
        operation = self._get(operation_id)

        self.session.delete(operation)
        self.session.commit()
