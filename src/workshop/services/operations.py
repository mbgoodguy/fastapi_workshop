from typing import List

from fastapi import Depends

from workshop import tables
from workshop.database import get_session, Session
from workshop.models.operations import OperationKind


class OperationService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self, kind: OperationKind) -> List[tables.Operation]:
        query = self.session.query(tables.Operation)
        if kind:
            query = query.filter_by(kind=kind)
        operations = query.all()
        return operations
