from pydantic import BaseModel, Field

class CategoryTypeBase(BaseModel):
  name: str = Field(max_length=50)
  language: int