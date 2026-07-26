from fastapi import FastAPI

app = FastAPI()

@app.get("/job/{job1}")
async def root(job1):
    return {"Job": job1}