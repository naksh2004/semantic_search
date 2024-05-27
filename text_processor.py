# text_processor.py

from fastapi import UploadFile

async def process_text(file: UploadFile):
    content = await file.read()
    text = content.decode('utf-8')
    return text
