from typing import Optional
from sqlmodel import SQLModel, Field, SMALLINT
from models import Language

class Profile(SQLModel, table=True):
  id: Optional[SMALLINT] = Field(default=None, primary_key=True)
  username: str = Field(max_length=50)
  slug: str = Field(max_length=100)
  fullname: str = Field(max_length=100)
  photo: Optional[str] = Field(max_length=200)
  phone_code: Optional[str] = Field(max_length=10)
  phone: Optional[str] = Field(max_length=20)
  email: Optional[str] = Field(max_length=100)

class ProfileTranslation(SQLModel, table=True):
  id: Optional[SMALLINT] = Field(default=None, primary_key=True)
  profile_id: SMALLINT = Field(foreign_key=Profile.id)
  position: str = Field(max_length=150)
  profile_details: str = Field(max_length=4000)
  cv: str = Field(max_length=200)
  language: SMALLINT = Field(foreign_key=Language.id)

