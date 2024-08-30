from typing import Optional
from sqlmodel import SQLModel, Field, SMALLINT

class Language(SQLModel, table=True):
  id: Optional[SMALLINT] = Field(default=None, primary_key=True)
  language_name: str = Field(max_length=100)
  slug: str = Field(max_length=100)
  iso: str = Field(max_length=2)