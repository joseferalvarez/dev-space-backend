from typing import Optional
from pydantic import BaseModel, Field

class ProfileBase(BaseModel):
  username: str = Field(max_length=50)
  fullname: str = Field(max_length=100)
  photo: Optional[str] = Field(max_length=200)
  phone_code: Optional[str] = Field(max_length=10)
  phone: Optional[str] = Field(max_length=20)
  email: Optional[str] = Field(max_length=100)

class ProfileTranslationBase(BaseModel):
  position: str = Field(max_length=150)
  profile_details: str = Field(max_length=4000)
  cv: str = Field(max_length=200)
  language: int = Field(foreign_key="language.id")