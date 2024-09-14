from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from database import connect, create_db
from src.languages.router import get_language_router
from src.contacts.router import get_contact_router
from src.technologies.router import get_technologies_router
from src.media.router import get_media_router
from src.social.router import get_social_router
from src.categories.router import get_category_router
from src.profiles.router import get_profile_router

app = FastAPI()
app.mount("/public", StaticFiles(directory="public"), name="public")

engine = connect()

app.include_router(get_language_router())
app.include_router(get_contact_router())
app.include_router(get_technologies_router())
app.include_router(get_media_router())
app.include_router(get_social_router())
app.include_router(get_category_router())
app.include_router(get_profile_router())

create_db()
