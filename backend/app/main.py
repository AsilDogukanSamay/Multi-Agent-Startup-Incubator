import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from backend.app.orchestrator import Orchestrator

# Initialize FastAPI
app = FastAPI(
    title="Multi-Agent Startup Incubator",
    description="Çoklu Ajanlı Girişim Kuluçka API Servisi",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request Models
class AnalyzeRequest(BaseModel):
    startup_idea: str

# API Endpoints
@app.post("/api/v1/incubator/analyze")
async def analyze_idea(request: AnalyzeRequest):
    if not request.startup_idea.strip():
        raise HTTPException(status_code=400, detail="Girişim fikri boş olamaz.")
    
    try:
        orchestrator = Orchestrator()
        result_memory = await orchestrator.run_incubator(request.startup_idea)
        return result_memory
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Kuluçka süreci sırasında hata oluştu: {str(e)}")

# Frontend Static File Serving
# Resolve path to the 'frontend' directory relative to 'backend/app'
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
frontend_path = os.path.join(base_dir, "frontend")

# Serve main index.html at root url
@app.get("/")
async def read_index():
    index_file = os.path.join(frontend_path, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return {"message": "Startup Incubator Backend is running. Frontend index.html not found."}

# Mount css and js subfolders if they exist
css_path = os.path.join(frontend_path, "css")
js_path = os.path.join(frontend_path, "js")

if os.path.exists(css_path):
    app.mount("/css", StaticFiles(directory=css_path), name="css")
if os.path.exists(js_path):
    app.mount("/js", StaticFiles(directory=js_path), name="js")
