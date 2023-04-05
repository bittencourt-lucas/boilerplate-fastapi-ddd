import re
from typing import Any

class Password:
    MIN_LENGTH = 8
    MAX_LENGTH = 32
    PATTERN = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
    
    def __init__(self, value: str) -> None:
        self.validate(value)
        self.value = value
        
    @classmethod
    def create(cls: Any, value: str) -> "Password":
        return cls(value)
    
    def validate(self, value: str) -> None:
        valid_password_length: bool = self.MIN_LENGTH <= len(value) <= self.MAX_LENGTH
        if not valid_password_length:
            raise ValueError(f"Password length must be between {self.MIN_LENGTH} and {self.MAX_LENGTH} characters.")
        if not re.match(self.PATTERN, value):
            raise ValueError("Password must contain at least one letter and one number.")
        
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Password):
            return False
        return self.value == other.value
    
    def __hash__(self) -> int:
        return hash(self.value)
    
    def __repr__(self) -> str:
        return f"Password({self.value})"
