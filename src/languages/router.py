from fastapi import APIRouter
from .schemas import LanguageCreate
from .service import LangService

router = APIRouter()
service = LangService


@router.get("/languages/", tags=["language"])
def get_languages():
   return {"languages": "test"}


@router.post("/language/", tags=["language"])
def post_language(language: LanguageCreate):
  result = service.post_language(language)
  return {"language": result}


def get_language_router():
    return router


if __name__ == "__main__":
  get_language_router()
