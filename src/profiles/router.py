from fastapi import APIRouter
from .service import ProfileService, ProfileTranslationService
from .schemas import ProfileBase, ProfileTranslationBase

router = APIRouter()
service = ProfileService
translation_service = ProfileTranslationService

@router.get("/profiles/", tags=["Profiles"])
async def get_profiles():
  return await service.get_profiles()

#@router.get("/profile/{id}/", tags=["Profiles", "Profile"])
#async def get_profile(id):
#  return await service.get_profile(id)

@router.get("/profile/{username}/", tags=["Profiles", "Profile"])
async def get_profile_by_username(username):
  return await service.get_profile_by_username(username)

@router.post("/profile/", tags=["Profiles", "Profile"])
async def post_profile(profile: ProfileBase):
  return await service.post_profile(profile)

@router.put("/profile/{id}/", tags=["Profiles", "Profile"])
async def put_profile(id: int, profile: ProfileBase):
  return await service.put_profile(id, profile)

@router.delete("/profile/{id}/", tags=["Profiles", "Profile"])
async def delete_profile(id: int):
  return await service.delete_profile(id)

@router.post("/profile-translation/{id}/", tags=["Profiles", "Profile", "Profile translation"])
async def post_profile_translation(id: int, profile_translation: ProfileTranslationBase):
  return await translation_service.post_profile_translation(id, profile_translation)

@router.put("/profile-translation/{id}/", tags=["Profiles", "Profile", "Profile translation"])
async def put_profile_translation(id: int, profile_translation: ProfileTranslationBase):
  return await translation_service.put_profile_translation(id, profile_translation)

@router.delete("/profile-translation/{id}/", tags=["Profiles", "Profile", "Profile translation"])
async def delete_profile_translation(id: int):
  return await translation_service.delete_profile_translation(id)

def get_profile_router():
  return router

if __name__ == "__main__":
  get_profile_router()