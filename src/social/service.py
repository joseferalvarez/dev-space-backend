from database import connect
from sqlmodel import Session, select
from .models import Social
from .schemas import SocialBase
from dependencies import generate_slug

class ServiceSocial:
  async def read_socials():
    with Session(connect()) as session:
      social = session.exec(select(Social)).all()
      return social
    
  async def read_social(id):
    with Session(connect()) as session:
      social = session.exec(select(Social).where(Social.id == id)).first()
      return social
    
  async def post_social(social: SocialBase):
    with Session(connect()) as session:
      new_social = Social(
        social_name=social.social_name,
        slug=generate_slug(social.social_name),
        link=social.link,
        icon=social.icon
      )

      session.add(new_social)
      session.commit()
      session.refresh(new_social)

      return new_social
  
  async def put_social(id: int, social: SocialBase):
    with Session(connect()) as session:
      new_social = session.exec(select(Social).where(Social.id == id)).first()

      new_social.social_name = social.social_name
      new_social.slug = generate_slug(social.social_name)
      new_social.link = social.link
      new_social.icon = social.icon

      session.add(new_social)
      session.commit()
      session.refresh(new_social)

      return new_social
  
  async def delete_social(id):
    with Session(connect()) as session:
      social = session.exec(select(Social).where(Social.id == id)).first()

      session.delete(social)
      session.commit()

      return social