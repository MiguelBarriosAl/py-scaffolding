from fastapi import HTTPException
from starlette.responses import JSONResponse
from constants import MAX


class Service:
    def __init__(self):
        self.load_files = []

    def add_file(self, file: dict):
        if len(self.load_files) < MAX:
            self.load_files.append(file)
            return JSONResponse(content=self.load_files, status_code=201)
        else:
            raise HTTPException(status_code=400, detail="File has been rejected (there are already 99 files)")

    def get_files(self):
        return JSONResponse(content={"files": self.load_files}, status_code=200)

    def get_file_id(self, id_file: str):
        for file in self.load_files:
            if file['id'] == id_file:
                return JSONResponse(content={"file": file['name']}, status_code=200)
        raise HTTPException(status_code=404, detail="Not Found")
