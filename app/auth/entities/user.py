from uuid import UUID, uuid4
from typing import List, Optional, Union, Any
from app.auth.value_objects.email import Email
from app.auth.value_objects.password import Password

class User:
    def __init__(self, email: Email, password: Password, id: Optional[UUID, str] = None) -> None:
        self.id = id or uuid4()
        self.email = email
        self.password = password
        
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, User):
            return False
        return self.id == other.id
    
    def __hash__(self) -> int:
        return hash(self.id)
    
    def __repr__(self) -> str:
        return f"User(id={self.id}, email={self.email})"
