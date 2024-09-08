from datetime import datetime
from pydantic import BaseModel, EmailStr, Field

class ContactBase(BaseModel):
  name: str = Field(max_length=50)
  phone: str = Field(max_length=16)
  email: EmailStr = Field(max_length=25)
  company: str = Field(max_length=50)
  message: str = Field(max_length=4000)

class ContactPostPut(ContactBase):
  pass

class ContactRead(ContactBase):
  id: str