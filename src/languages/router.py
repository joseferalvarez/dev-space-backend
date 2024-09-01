from fastapi import APIRouter
from .schemas import LanguagePost, LanguageTranslationPost, LanguagePut, LanguageTranslationPut
from .service import LangService

router = APIRouter()
service = LangService

# Languages router
@router.get("/languages/", tags=["languages"])
def get_languages():
  languages = service.get_languages()
  return languages

# Language router
@router.get("/language/{id}", tags=["languages", "language"])
def get_language(id):
  language = service.get_language(language_id=id)
  return language

@router.post("/language/", tags=["languages", "language"])
def post_language(language: LanguagePost):
  language = service.post_language(language)
  return language

@router.put("/language/", tags=["languages", "language"])
def put_language(language: LanguagePut):
  language = service.put_language(language)
  return language

@router.delete("/language/{id}", tags=["languages", "language"])
def delete_language(id):
  language = service.delete_language(id)
  return language

# Translation router
@router.get("/language-translation/{id}", tags=["languages", "language", "translation"])
def get_language(id):
  translation = service.get_translation(id)
  return translation

@router.post("/language-translation/", tags=["languages", "language", "translation"])
def post_translation(language: LanguageTranslationPost):
  translation = service.post_translation(language)
  return translation

@router.put("/language-translation/", tags=["languages", "language", "translation"])
def put_translation(translation: LanguageTranslationPut):
  translation = service.put_translation(translation)
  return translation

@router.delete("/language-translation/{id}", tags=["languages", "language", "translation"])
def delete_translation(id):
  translation = service.delete_translation(id)
  return translation

def get_language_router():
    return router


if __name__ == "__main__":
  get_language_router()
