from fastapi import APIRouter
from .service import ServiceSocial
from .schemas import SocialBase

router = APIRouter()
service = ServiceSocial

def get_social_router():
  return router

@router.get("/socials/", tags=["socials"])
async def get_socials():
  return await service.read_socials()

@router.get("/social/{id}/", tags=["socials", "social"])
async def get_social(id: int):
  return await service.read_social(id)

@router.post("/social/", tags=["socials", "social"])
async def post_social(social: SocialBase):
  return await service.post_social(social)

@router.put("/social/{id}/", tags=["socials", "social"])
async def put_social(id: int, social: SocialBase):
  return await service.put_social(id, social)

@router.delete("/social/{id}/", tags=["socials", "social"])
async def delete_social(id: int):
  return await service.delete_social(id)

if __name__ == "__main__":
  get_social_router()