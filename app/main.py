from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
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

# Mount the 'ui' directory to serve static files
app.mount("/ui", StaticFiles(directory="ui"), name="ui")

# Default route to serve index.html
@app.get("/", response_class=HTMLResponse)
async def read_index():
    index_path = os.path.join("ui", "index.html")
    with open(index_path, "r") as f:
        return f.read()

# API routes
app.include_router(predict_router, prefix="/api")
