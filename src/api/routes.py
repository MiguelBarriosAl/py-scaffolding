from fastapi import FastAPI, APIRouter, Request
from starlette.responses import JSONResponse
from fastapi import HTTPException
from api.app import App
from api.models import File
from constants import IP_CACHE, TIME, __version__

app = FastAPI()
api = App()
router = APIRouter()


@app.get("/health")
def status():
    response = {
        "HealthCheck": "Ok",
        "Version": __version__}
    return JSONResponse(content=response, media_type="application/json")


@app.post("/files")
async def upload_file(file: File) -> list:
    global api
    data = {"id": file.id, "name": file.name, "url": file.url}
    registered = api.file(data)
    return registered


@app.get("/files")
async def get_all_files() -> dict:
    api.get_files()
    return api.get_files()


@app.get("/files/{id_file}")
async def get_file_by_id(id_file: str, request: Request) -> dict:
    ip_address = request.client.host
    if ip_address in IP_CACHE and IP_CACHE[ip_address] >= TIME:
        raise HTTPException(status_code=429, detail="Rate limit exceeded. Try again in 1 minute.")
    api.get_file_id(id_file)
    return api.get_file_id(id_file)


app.include_router(router)
