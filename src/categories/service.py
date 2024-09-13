from database import connect
from sqlmodel import  Session, select
from .models import CategoryType, CategoryTypeTranslation
from .schemas import CategoryTypeBase
from src.languages.models import Language

class CategoryTypeService:
  async def get_category_types():
    with Session(connect()) as session:
      category_types = session.exec(select(CategoryType)).all()
      categories = []

      for category_type in category_types:
        category = {
          "id": category_type.id,
          "name": category_type.name,
          "translations": {}
        }
        category_translations = session.exec(select(CategoryTypeTranslation).where(CategoryTypeTranslation.category_type == category_type.id)).all()

        for category_translation in category_translations:
          language = session.exec(select(Language).where(Language.id == category_translation.language)).first()
          category["translations"][language.iso] = category_translation
        
        categories.append(category)
      
      return categories
  
  async def get_category_type(id):
    with Session(connect()) as session:
      category_type = session.exec(select(CategoryType).where(CategoryType.id == id)).first()

      category = {
        "id": category_type.id,
        "name" : category_type.name,
        "translations": {}
      }

      category_translations = session.exec(select(CategoryTypeTranslation).where(CategoryTypeTranslation.category_type == category_type.id)).all()

      for category_translation in category_translations:
        language = session.exec(select(Language).where(Language.id == category_translation.language)).first()

        category["translations"][language.iso] = category_translation
      
      return category
  
  async def post_category_type(category_type: CategoryTypeBase):
    with Session(connect()) as session:
      category = CategoryType(name=category_type.name)

      session.add(category)
      session.commit()
      session.refresh(category)

      category_translation = CategoryTypeTranslation(category_type=category.id, category_name=category_type.name, language=category_type.language)
      session.add(category_translation)
      session.commit()
      session.refresh(category_translation)

      return {
        "id": category.id,
        "name": category.name,
        "translations": category_translation
      }
  
  async def delete_category_type(id):
    with Session(connect()) as session:
      category_translations = session.exec(select(CategoryTypeTranslation).where(CategoryTypeTranslation.category_type == id)).all()

      for category_translation in category_translations:
        session.delete(category_translation)
      
      category = session.exec(select(CategoryType).where(CategoryType.id == id)).first()
      session.delete(category)

      session.commit()

      return category