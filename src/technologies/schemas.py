from typing import Optional
from pydantic import BaseModel, Field

class TechnologyBase(BaseModel):
  technology_name: str = Field(max_length=20)
  link: Optional[str] = Field(max_length=200)
  icon: Optional[str]