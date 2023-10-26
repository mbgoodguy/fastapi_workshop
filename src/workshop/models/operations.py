from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class OperationKind(str, Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'


class Operation(BaseModel):
    id: int
    data: date
    kind: OperationKind
    description: str
    amount: Optional[str]
