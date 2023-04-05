from uuid import UUID
from typing import Optional, List
from app.auth.value_objects.email import Email
from app.auth.entities.user import User
from app.auth.repositories.user_repository import UserRepository

class UserRepository(UserRepository):
    users: List[User] = []
  
    def save(self, user: User):
        self.users.append(user)
        return user
    
    def get_by_id(self, user_id: UUID) -> Optional[User]:
        user: Optional[User] = next((user for user in self.users if user.id == user_id), None)
        return user
    
    def get_by_email(self, user_email: Email) -> Optional[User]:
        user: Optional[User] = next((user for user in self.users if user.email == user_email), None)
        return user
    