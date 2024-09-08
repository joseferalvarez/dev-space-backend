from fastapi import APIRouter
from .schemas import ContactBase
from .service import ContactService

router = APIRouter()
service = ContactService

@router.get("/contacts/", tags=["contacts"])
def get_contacts():
  contacts = service.get_contacts()
  return contacts

@router.get("/contact/{id}/", tags=["contacts", "contact"])
def get_contact(id):
   contact = service.get_contact(id)
   return contact

@router.post("/contact/", tags=["contacts", "contact"])
def post_contact(contact: ContactBase):
   new_contact = service.post_contact(contact)
   return new_contact

@router.delete("/contact/{id}/", tags=["contacts", "contact"])
def delete_contact(id):
   contact = service.delete_contact(id)
   return contact

def get_contact_router():
    return router

if __name__ == "__main__":
  get_contact_router()