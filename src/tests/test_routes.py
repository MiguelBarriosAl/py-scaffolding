import unittest
from fastapi.testclient import TestClient
from src.api.routes import app

client = TestClient(app)


class TestFileUpload(unittest.TestCase):
    def test_upload_file(self):
        file = {"id": "1", "name": "test.txt", "url": "https://99files.com"}
        response = client.post("/files", json=file)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), [{"id": "1", "name": "test.txt", "url": "https://99files.com"}])

    def test_upload_empty_file(self):
        file = {}
        response = client.post("/files", json=file)
        self.assertEqual(response.status_code, 422)


class TestGetAllFiles(unittest.TestCase):
    def test_get_all_files(self):
        response = client.get("/files")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"files": []})


class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = TestClient(app)

    def test_upload_file(self):
        file = {"id": "1", "name": "test.txt", "url": "https://99files.com"}
        response = self.app.post("/files", json=file)
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()


