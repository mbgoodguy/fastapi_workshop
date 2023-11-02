from typing import List

from fastapi import Depends

from workshop import tables
from workshop.database import get_session, Session


class OperationService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self) -> List[tables.Operation]:
        operations = (
            self.session
            .query(tables.Operation)
            .all()
        )
        return operations
