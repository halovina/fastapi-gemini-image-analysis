from fastapi import FastAPI, UploadFile, Form
from typing import Annotated
from PIL import Image
from gemini import send_prompt_flash

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/upload-file")
def upload_file_to_text(upload_file: UploadFile, prompt_text: Annotated[str, Form()]):
    fileimage = Image.open(upload_file.file)
    
    response = send_prompt_flash(fileimage, prompt_text)
    
    print(response.text)
    
    return {
        "message": response.text
    }