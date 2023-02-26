from src.api.services import Service


class App:
    def __init__(self):
        self.service = Service()

    def file(self, file: dict) -> dict:
        files = self.service.add_file(file)
        return files

    def get_files(self) -> list:
        return self.service.get_files()

    def get_file_id(self, id_file: str):
        return self.service.get_file_id(id_file)




