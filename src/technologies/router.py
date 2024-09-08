from fastapi import APIRouter
from .service import ServiceTechnology
from .schemas import TechnologyBase

router = APIRouter()
service = ServiceTechnology

@router.get("/technologies/", tags=["technologies"])
def get_technologies():
  technologies = service.get_technologies()
  return technologies

@router.get("/technology/{id}/", tags=["technologies", "technology"])
def get_technology(id):
  tech = service.delete_technology(id)
  return tech

@router.post("/technology/", tags=["technologies", "technology"])
def post_technology(technology: TechnologyBase):
  tech = service.post_technology(technology)
  return tech

@router.put("/technology/{id}/", tags=["technologies", "technology"])
def put_technology(id, technology: TechnologyBase):
  tech = service.put_technology(id, technology)
  return tech

@router.delete("/technology/{id}/", tags=["technologies", "technology"])
def delete_technology(id):
  tech = service.delete_technology(id)
  return tech

def get_technologies_router():
  return router

if __name__ == "__main__":
  get_technologies_router()