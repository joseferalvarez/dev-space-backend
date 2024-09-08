from typing import Optional
from sqlmodel import SQLModel, Field

class Technology(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  technology_name: str = Field(max_length=20)
  slug: str = Field(max_length=20)
  link: Optional[str] = Field(max_length=200)
  icon: Optional[str] = Field(max_length=200)