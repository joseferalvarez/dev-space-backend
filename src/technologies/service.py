from database import connect
from sqlmodel import Session, select
from .models import Technology
from .schemas import TechnologyBase
from dependencies import generate_slug

class ServiceTechnology:
  async def get_technologies():
    """get all the technologies"""
    with Session(connect()) as session:
      technologies = session.exec(select(Technology)).all()
      return technologies
  
  async def get_technology(id):
    """get a technology by it's id"""
    with Session(connect()) as session:
      technology = session.exec(select(Technology).where(Technology.id == id)).first()
      return technology
    
  async def post_technology(technology: TechnologyBase):
    """post a new technology (technology_name, slug, link, icon)"""
    with Session(connect()) as session:
      new_technology = Technology(
        technology_name=technology.technology_name,
        slug=generate_slug(technology.technology_name),
        link=technology.link,
        icon=technology.icon
      )

      session.add(new_technology)
      session.commit()
      session.refresh(new_technology)

      return new_technology
  
  async def put_technology(id: int, technology: TechnologyBase):
    """update an existing technology (id, [technology_name, link, icon])"""
    with Session(connect()) as session:
      current_tech = session.exec(select(Technology).where(Technology.id == id)).first()

      if current_tech:
        if technology.technology_name: 
          current_tech.technology_name = technology.technology_name
          current_tech.slug = generate_slug(technology.technology_name)

        if technology.link:
          current_tech.link = technology.link

        if technology.icon:
          current_tech.icon = technology.icon
      
      session.add(current_tech)
      session.commit()
      session.refresh(current_tech)

      return current_tech
  
  async def delete_technology(id: int):
    """delete a technology by it's id"""
    with Session(connect()) as session:
      tech = session.exec(select(Technology).where(Technology.id == id)).first()

      if tech:
        session.delete(tech)
        session.commit()
      
      return tech