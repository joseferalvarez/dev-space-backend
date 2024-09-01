from pydantic import BaseModel

class LanguageTranslationRead(BaseModel):
  """pydantic class to read a language translation"""
  id: int
  language_id: int
  language_iso: str
  language_name: str
  slug: str

class LanguageRead(BaseModel):
  """pydantic class to read a language with its tranlations"""
  id: int
  iso: str
  translations: dict[str, LanguageTranslationRead]

class LanguagePost(BaseModel):
  """pydantic class to post a new language"""
  language_name: str
  iso: str

class LanguagePostRead(BaseModel):
  """pydantic class to read a language"""
  id: int
  iso: str
  language_name: str
  slug: str