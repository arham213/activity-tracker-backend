from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

from app.routers import imageToText

load_dotenv()

app = FastAPI(title="Activity Tracker API", version="1.0.0")

allowed_origins = os.getenv("ALLOWED_ORIGINS", "https://activity-tracker-frontend-eta.vercel.app").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(imageToText.router)

@app.get("/")
def root():
    return {"message": "Activity Tracker API is running"}