from pydantic import EmailStr
from typing import Any

class Email:
    def __init__(self, value: EmailStr) -> None:
        self.value = value
        
    @classmethod
    def create(cls: Any, value: str) -> "Email":
        email = EmailStr(value)
        return cls(email)
    
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Email):
            return False
        return self.value == other.value
    
    def __hash__(self) -> int:
        return hash(self.value)
    
    def __repr__(self) -> str:
        return f"Email({self.value})"
    