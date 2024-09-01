from fastapi import HTTPException
from sqlmodel import Session, select
from .models import Language, LanguageTranslation
from .schemas import (
  LanguagePost, 
  LanguageRead, 
  LanguagePostRead, 
  LanguageTranslationPost, 
  LanguageTranslationRead, 
  LanguagePut,
  LanguageTranslationPut
)
from database import connect
from dependencies import generate_slug

#TODO: control the ISO length
class LangService():
  def get_languages():
    """get all the languages"""
    with Session(connect()) as session:
      langs = []
      languages = session.exec(select(Language)).all()

      for language in languages:
        translations = session.exec(select(LanguageTranslation).where(LanguageTranslation.language_id == language.id)).all()
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
    
  def get_language(language_id: int):
    """gets a language by its id"""
    with Session(connect()) as session:
      language = session.exec(select(Language).where(Language.id == language_id)).first()
      translations = session.exec(select(LanguageTranslation).where(LanguageTranslation.language_id == language_id)).all()

      lang = LanguageRead(id=language.id, iso=language.iso, translations={})

      for translation in translations:
        lang.translations[translation.language_iso] = translation

      return lang
    
  def put_language(language: LanguagePut):
    with Session(connect()) as session:
      current_language = session.exec(select(Language).where(Language.id == language.id)).first()
      current_language.iso = language.iso
      session.add(current_language)
      session.commit()
      session.refresh(current_language)
      print(current_language)
      translations = session.exec(select(LanguageTranslation).where(LanguageTranslation.language_id == current_language.id)).all()

      lang = LanguageRead(id=current_language.id, iso=current_language.iso, translations={})

      for translation in translations:
        lang.translations[translation.language_iso] = translation
      
      return lang
    
  def delete_language(id):
    with Session(connect()) as session:
      language = session.exec(select(Language).where(Language.id == id)).first()
      translations = session.exec(select(LanguageTranslation).where(LanguageTranslation.language_id == id)).all()

      lang = LanguageRead(id=language.id, iso=language.iso, translations={})

      for translation in translations:
        lang.translations[translation.language_iso] = translation
        session.delete(translation)
        session.commit()
      
      session.delete(language)
      session.commit()

      return lang

    
  # Translation functions  
  def get_translation(id):
    with Session(connect()) as session:
      translation = session.exec(select(LanguageTranslation).where(LanguageTranslation.id == id)).first()

      if not translation:
        return HTTPException(status_code=404, detail="Translation not found")

      return LanguageTranslationRead(
        id=translation.id,
        language_id=translation.language_id,
        language_iso=translation.language_iso,
        language_name=translation.language_name,
        slug=translation.slug
      )

  def post_translation(translation: LanguageTranslationPost):
    with Session(connect()) as session:

      translation = LanguageTranslation(
          language_id=translation.language_id,
          language_iso=translation.language_iso,
          language_name=translation.language_name,
          slug=generate_slug(translation.language_name)
        )
      
      session.add(translation)
      session.commit()
      session.refresh(translation)

      return LanguageTranslationRead(
        id=translation.id,
        language_id=translation.language_id,
        language_iso=translation.language_iso,
        language_name=translation.language_name,
        slug=translation.slug
      )
    
  def put_translation(translation: LanguageTranslationPut):
    with Session(connect()) as session:
      current_translation = session.exec(select(LanguageTranslation).where(LanguageTranslation.id == translation.id)).first()
      current_translation.language_iso = translation.language_iso
      current_translation.language_name = translation.language_name
      current_translation.slug = generate_slug(current_translation.language_name)

      session.add(current_translation)
      session.commit()
      session.refresh(current_translation)

      return LanguageTranslationRead(
        id=current_translation.id,
        language_id=current_translation.language_id,
        language_iso=current_translation.language_iso,
        language_name=current_translation.language_name,
        slug=current_translation.slug
      )
  
  def delete_translation(id):
    with Session(connect()) as session:
      translation = session.exec(select(LanguageTranslation).where(LanguageTranslation.id == id)).first()
      session.delete(translation)
      session.commit()

      return LanguageTranslationRead(
        id=translation.id,
        language_id=translation.language_id,
        language_iso=translation.language_iso,
        language_name=translation.language_name,
        slug=translation.slug
      )