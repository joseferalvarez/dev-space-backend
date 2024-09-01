from fastapi import APIRouter
from .schemas import LanguagePost
from .service import LangService

router = APIRouter()
service = LangService


@router.get("/languages/", tags=["language"])
def get_languages():
  languages = service.get_languages()
  return {"languages": languages}


@router.post("/language/", tags=["language"])
def post_language(language: LanguagePost):
  result = service.post_language(language)
  return {"language": result}


def get_language_router():
    return router


if __name__ == "__main__":
  get_language_router()
