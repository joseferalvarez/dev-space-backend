from sqlmodel import Session, select
from .models import Language, LanguageTranslation
from .schemas import LanguagePost, LanguageRead, LanguagePostRead
from database import connect
from dependencies import generate_slug

class LangService():
  def get_languages():
    """get all the languages"""
    with Session(connect()) as session:
      langs = []
      results = session.exec(select(Language))
      languages = results.all()

      for language in languages:
        results = session.exec(select(LanguageTranslation).where(LanguageTranslation.language_id == language.id))
        translations = results.all()
        lang = LanguageRead(id=language.id, iso=language.iso, translations={})

        for translation in translations:
          lang.translations[translation.language_iso] = translation
        
        langs.append(lang)
      
      return langs


  def post_language(language=LanguagePost):
    """posts a new language"""
    with Session(connect()) as session:
      lang = Language(iso=language.iso)

      session.add(lang)
      session.commit()
      session.refresh(lang)

      lang_translation = LanguageTranslation(language_id=lang.id, language_iso=lang.iso, language_name=language.language_name, slug=generate_slug(language.language_name))

      session.add(lang_translation)
      session.commit()
      session.refresh(lang_translation)

      return LanguagePostRead(id=lang.id, iso=lang.iso, language_name=lang_translation.language_name, slug=lang_translation.slug)