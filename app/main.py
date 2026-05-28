from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import analyze, letter

app = FastAPI(
    title="CareerPulse AI Backend",
    description="Structured FastAPI + Machine Learning Resume Matching System",
    version="1.0.0"
)

# Setup CORS so the React frontend on any port can access it directly during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routers
app.include_router(analyze.router)
app.include_router(letter.router)

@app.get("/")
def read_root():
    return {"status": "running", "service": "CareerPulse API"}
