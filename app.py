# coding: utf-8
#!/usr/bin/python3
#!flask/bin/python3
import os
import uvicorn

from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

#Nominalization Library
import nominalize 

main = FastAPI()

origins = ["*"]

main.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@main.get("/nominal/{text}")
async def nominal(text):
    text = "{} means ".format(text)
    result = nominalize.get_nom(text)
    return result

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)    


