from typing import Optional
from datetime import date
from sqlmodel import SQLModel, Field

class Contact(SQLModel):
  id: int = Field(default=None, primary_key=True)
  name: str = Field(max_length=50)
  phone: Optional[str] = Field(max_length=16)
  email: str = Field(max_length=25)
  company: Optional[str] = Field(max_length=50)
  message: Optional[str] = Field(max_length=4000)
  date_send: date