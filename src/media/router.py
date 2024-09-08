from fastapi import APIRouter, UploadFile
from .service import MediaService


router = APIRouter()
service = MediaService()

@router.get("/files/", tags=["media"])
async def get_files():
  res = await service.get_files()
  return res

@router.post("/files/upload/", tags=["media"])
async def upload_file(file: UploadFile):
  res = await service.upload_file(file)
  return res

@router.delete("/files/delete/{file}", tags=["media"])
async def delete_file(file: str):
  res = await service.delete_file(file)
  return res

def get_media_router():
  return router

if __name__ == "__main__":
  get_media_router()