from sqlmodel import SQLModel, Field
from typing import Optional

class CategoryType(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  name: str = Field(max_length=50)

class CategoryTypeTranslation(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  category_type: int = Field(foreign_key="categorytype.id")
  category_name: str = Field(max_length=50)
  language: int = Field(foreign_key="language.id")

class Category(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  name: str = Field(max_length=50)
  category_type: Optional[int]

class CategoryTranslation(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  category_id: int = Field(foreign_key="category.id")
  category_name: str = Field(max_length=50)
  slug: str = Field(max_length=50)
  language: int = Field(foreign_key="language.id")