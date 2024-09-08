from fastapi import HTTPException
from sqlmodel import Session, select
from .schemas import ContactBase
from .models import Contact
from database import connect
import datetime

class ContactService():
  def get_contacts():
    """get all the contacts"""
    with Session(connect()) as session:
      contacts = session.exec(select(Contact)).all()
      return contacts
  
  def get_contact(id: int):
    """get a contact by it's id (id)"""
    with Session(connect()) as session:
      contact = session.exec(select(Contact).where(Contact.id == id)).first()
      print(id)
      return contact
  
  def post_contact(contact: ContactBase):
    """post a new contact (name, phone, email, company, message)"""
    with Session(connect()) as session:
      new_contact = Contact(
        name=contact.name,
        phone=contact.phone,
        email=contact.email,
        company=contact.company,
        message=contact.message,
        date_send=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      )

      session.add(new_contact)
      session.commit()
      session.refresh(new_contact)

      return new_contact
  
  def delete_contact(id: int):
    """delete a contact by it's id"""
    with Session(connect()) as session:
      contact = session.exec(select(Contact).where(Contact.id == id)).first()
      if contact:
        session.delete(contact)
        session.commit()
      
      return contact
