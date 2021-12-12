from fastapi import FastAPI

app = FastAPI(title="One Voice Api", description="The backend for One Voice", version="1")

@app.get("/")
async def index():
    return "Helo world"