from fastapi import UploadFile, HTTPException
import os

class MediaService():
  async def get_files(self):
    """get all files from """
    return {"files": os.listdir("./public/")}


  async def upload_file(self, file: UploadFile):
    """Upload a new file"""
    path = f"./public/{file.filename}"
    
    if os.path.exists(path):
      return HTTPException(status_code=409, detail="The file already exists")
  
    with open(path, "wb+") as new_file:
      new_file.write(await file.read())
  
    return {"file": file.filename, "size": file.size, "type": file.content_type}
  

  async def delete_file(self, file: str):
    """Delete a existing file"""
    path = f"./public/{file}"

    if not os.path.exists(path):
      return HTTPException(status_code=404, detail="File not found")
    
    os.remove(path)

    if os.path.exists(path):
      return HTTPException(status_code=409, detail="The file can not be removed")
    else:
      return {"detail": "The file was succesfully removed"}