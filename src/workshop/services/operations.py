from typing import List

from fastapi import Depends

from workshop import tables
from workshop.database import Session, get_session


class OperationService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self) -> List[tables.Operation]:
        # перенесли сюда логику из api/operations
        operations = (
            self.session
            .query(tables.Operation)
            .all()
        )
        return operations
