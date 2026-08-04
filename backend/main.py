
from fastapi import FastAPI
import jobs.api as jobs_api
app = FastAPI()
app.include_router(jobs_api.router)

@app.get("/")
async def root():
    return {"message": "This is the main entry of the bigger application"}

@app.get("/health")
async def get_health():
    return {"message": "Server is running"}