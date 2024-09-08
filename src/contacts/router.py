from fastapi import APIRouter
from .schemas import ContactBase
from .service import ContactService

router = APIRouter()
service = ContactService

@router.get("/contacts/", tags=["contacts"])
async def get_contacts():
  contacts = await service.get_contacts()
  return contacts

@router.get("/contact/{id}/", tags=["contacts", "contact"])
async def get_contact(id):
   contact = await service.get_contact(id)
   return contact

@router.post("/contact/", tags=["contacts", "contact"])
async def post_contact(contact: ContactBase):
   new_contact = await service.post_contact(contact)
   return new_contact

@router.delete("/contact/{id}/", tags=["contacts", "contact"])
async def delete_contact(id):
   contact = await service.delete_contact(id)
   return contact

def get_contact_router():
    return router

if __name__ == "__main__":
  get_contact_router()