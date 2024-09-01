import re
from unidecode import unidecode

def generate_slug(text):
  text = unidecode(text)
  text = re.sub(r'[^\w\s-]', '-', text)
  text = re.sub(r'[-\s]+', '-', text).strip("-")
  text = text.lower()
  return text
