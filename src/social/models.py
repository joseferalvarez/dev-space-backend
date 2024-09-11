from typing import Optional
from sqlmodel import SQLModel, Field

class Social(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  social_name: str = Field(max_length=50)
  slug: str = Field(max_length=50)
  link: Optional[str] = Field(max_length=200)
  icon: Optional[str] = Field(max_length=200)