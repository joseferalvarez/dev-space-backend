from database import connect
from sqlmodel import Session, select
from dependencies import generate_slug
from .models import Profile, ProfileTranslation
from .schemas import ProfileBase, ProfileTranslationBase
from src.languages.models import Language

class ProfileService:
  async def get_profiles():
    with Session(connect()) as session:
      profiles = session.exec(select(Profile)).all()
      profile_list = []

      for profile in profiles:
        profile_dict = {
          "id": profile.id,
          "username": profile.username,
          "slug": profile.slug,
          "fullname": profile.fullname,
          "photo": profile.photo,
          "phone_code": profile.phone_code,
          "phone": profile.phone,
          "email": profile.email,
          "translations": {}
        }
        profile_translations = session.exec(select(ProfileTranslation).where(ProfileTranslation.profile_id == profile.id)).all()
        for profile_translation in profile_translations:
          language = session.exec(select(Language).where(Language.id == profile_translation.language)).first()
          profile_dict["translations"][language.iso] = profile_translation
        
        profile_list.append(profile_dict)

      return profile_list
  
  async def get_profile(id):
    with Session(connect()) as session:
      profile = session.exec(select(Profile).where(Profile.id == id)).first()
      return profile
    
  async def get_profile_by_username(username: str):
    with Session(connect()) as session:
      profile = session.exec(select(Profile).where(Profile.username == username)).first()
      return profile
  
  async def post_profile(profile: ProfileBase):
    with Session(connect()) as session:
      profile = Profile(
        username=profile.username,
        slug=generate_slug(profile.fullname),
        fullname=profile.fullname,
        photo=profile.photo,
        phone_code=profile.phone_code,
        phone=profile.phone,
        email=profile.email
      )
      session.add(profile)
      session.commit()
      session.refresh(profile)

      return profile
  
  async def put_profile(id: int, profile: ProfileBase):
    with Session(connect()) as session:
      new_profile = session.exec(select(Profile).where(Profile.id == id)).first()

      new_profile.username = profile.username
      new_profile.slug = generate_slug(profile.fullname)
      new_profile.fullname = profile.fullname
      new_profile.photo = profile.photo
      new_profile.phone_code = profile.phone_code
      new_profile.phone = profile.phone
      new_profile.email = profile.email

      session.add(new_profile)
      session.commit()
      session.refresh(new_profile)

      return new_profile
    
  async def delete_profile(id:int):
    with Session(connect()) as session:
      profile = session.exec(select(Profile).where(Profile.id == id)).first()
      session.delete(profile)
      session.commit()

      return profile
    

class ProfileTranslationService:
  async def post_profile_translation(id: int, profile_translation: ProfileTranslationBase):
    with Session(connect()) as session:
      profile = ProfileTranslation(
        profile_id=id,
        position=profile_translation.position,
        profile_details=profile_translation.profile_details,
        cv=profile_translation.cv,
        language=profile_translation.language
      )

      session.add(profile)
      session.commit()
      session.refresh(profile)

      return profile
  
  async def put_profile_translation(id: int, profile_translation: ProfileTranslationBase):
    with Session(connect()) as session:
      profile = session.exec(select(ProfileTranslation).where(ProfileTranslation.id == id)).first()

      profile.position = profile_translation.position
      profile.profile_details = profile_translation.profile_details
      profile.cv = profile_translation.profile_details

      session.add(profile)
      session.commit()
      session.refresh(profile)

      return profile
  
  async def delete_profile_translation(id: int):
    with Session(connect()) as session:
      profile = session.exec(select(ProfileTranslation).where(ProfileTranslation.id == id)).first()
      session.delete(profile)
      session.commit()

      return profile