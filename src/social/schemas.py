from typing import Optional
from pydantic import BaseModel, Field

class SocialBase(BaseModel):
  profile_username: str = Field(max_length=50)
  social_name: str = Field(max_length=50)
  social_username: str = Field(max_length=50)
  link: Optional[str] = Field(max_length=200)
  icon: Optional[str] = Field(max_length=200)