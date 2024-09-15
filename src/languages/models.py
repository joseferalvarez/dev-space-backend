from typing import Optional
from sqlalchemy import UniqueConstraint
from sqlmodel import SQLModel, Field

class Language(SQLModel, table=True):
  """Language class (iso)"""
  __table_args__ = (UniqueConstraint('iso'),)
  id: Optional[int] = Field(default=None, primary_key=True)
  iso: str = Field(max_length=2, unique=True)

class LanguageTranslation(SQLModel, table=True):
  """Language translation class (language_name, slug)"""
  id: Optional[int] = Field(default=None, primary_key=True)
  language_id: int = Field(foreign_key="language.id")
  language_iso: str = Field(max_length=2)
  language_name: str = Field(max_length=25)
  slug: str = Field(max_length=25)