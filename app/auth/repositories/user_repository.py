import abc
from uuid import UUID
from typing import Optional
from app.auth.value_objects.email import Email
from app.auth.entities.user import User

class UserRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, user: User):
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_by_id(self, user_id: UUID) -> Optional[User]:
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_by_email(self, user_email: Email) -> Optional[User]:
        raise NotImplementedError
    