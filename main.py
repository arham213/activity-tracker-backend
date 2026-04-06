from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import imageToText

app = FastAPI(title="Activity Tracker API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(imageToText.router)

@app.get("/")
def root():
    return {"message": "Activity Tracker API is running"}