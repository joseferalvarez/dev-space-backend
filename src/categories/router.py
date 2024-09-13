from fastapi import APIRouter
from .service import CategoryTypeService
from .schemas import CategoryTypeBase

router = APIRouter()
service = CategoryTypeService

@router.get("/category-types/", tags=["Category types"])
async def get_category_types():
  return await service.get_category_types()

@router.get("/category-type/{id}/", tags=["Category types", "category type"])
async def get_category_type(id: int):
  return await service.get_category_type(id)

@router.post("/category-type/", tags=["Category types", "Category type"])
async def post_category_type(category_type: CategoryTypeBase):
  return await service.post_category_type(category_type)

@router.delete("/category-type/{id}/", tags=["Category types", "Category type"])
async def delete_category_type(id):
  return await service.delete_category_type(id)

def get_category_router():
  return router

if __name__ == "__main__":
  get_category_router()