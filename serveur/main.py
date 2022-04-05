import uvicorn
from fastapi.applications import FastAPI
from router import router

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port="8000", log_level="info")
