from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.api.predict import router as predict_router
import os

app = FastAPI(title="Iris Classifier API")

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the 'static' folder
app.mount("/static", StaticFiles(directory=os.path.join("ui", "static")), name="static")

# Templates folder
templates = Jinja2Templates(directory=os.path.join("ui", "templates"))

# Serve index.html
@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# API routes
app.include_router(predict_router, prefix="/api")
