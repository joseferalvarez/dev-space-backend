from fastapi import APIRouter
from .service import ServiceTechnology
from .schemas import TechnologyBase

router = APIRouter()
service = ServiceTechnology

@router.get("/technologies/", tags=["technologies"])
async def get_technologies():
  technologies = await service.get_technologies()
  return technologies

@router.get("/technology/{id}/", tags=["technologies", "technology"])
async def get_technology(id):
  tech = await service.delete_technology(id)
  return tech

@router.post("/technology/", tags=["technologies", "technology"])
async def post_technology(technology: TechnologyBase):
  tech = await service.post_technology(technology)
  return tech

@router.put("/technology/{id}/", tags=["technologies", "technology"])
async def put_technology(id, technology: TechnologyBase):
  tech = await service.put_technology(id, technology)
  return tech

@router.delete("/technology/{id}/", tags=["technologies", "technology"])
async def delete_technology(id):
  tech = await service.delete_technology(id)
  return tech

def get_technologies_router():
  return router

if __name__ == "__main__":
  get_technologies_router()