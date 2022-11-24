from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from Apps.routes.mahasiswa import router as mahasiswa_router
import uvicorn

app = FastAPI()

app.mount("/public", StaticFiles(directory="public"), name="public")

app.include_router(mahasiswa_router)


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
