from sqlmodel import Session
from .models import Language, LanguageTranslation
from .schemas import LanguageCreate, LanguageRead
from database import connect

class LangService():
  def post_language(language=LanguageCreate):
    """posts a new language"""
    with Session(connect()) as session:
      lang = Language(iso=language.iso)

      session.add(lang)
      session.commit()
      session.refresh(lang)

      lang_translation = LanguageTranslation(language_id=lang.id, language_name=language.language_name, slug="test")

      session.add(lang_translation)
      session.commit()
      session.refresh(lang_translation)

      return LanguageRead(id=lang.id, iso=lang.iso, language_name=lang_translation.language_name, slug=lang_translation.slug)