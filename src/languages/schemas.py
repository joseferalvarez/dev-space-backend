from pydantic import BaseModel

class LanguageCreate(BaseModel):
  """pydantic class to post a new language"""
  language_name: str
  iso: str

class LanguageRead(BaseModel):
  """pydantic class to read a language"""
  id: int
  iso: str
  language_name: str
  slug: str

class LanguageTranslationRead(BaseModel):
  """pydantic class to read a language translation"""
  id: int
  language_name: str
  slug: str