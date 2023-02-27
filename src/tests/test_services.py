import unittest
from unittest.mock import patch
from fastapi import status, HTTPException
from api.models import File
from api.services import Service


class TestService(unittest.TestCase):
    def setUp(self):
        self.service = Service()

    @patch("api.services.MAX", 99)
    def test_add_file(self):
        # test adding a file
        file = File(id="1", name="test.txt", url="http://99files.com/file1")
        response = self.service.add_file(file.dict())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # test adding 100 files
        self.service.load_files = [file.dict()] * 100
        with self.assertRaises(HTTPException) as cm:
            self.service.add_file(file.dict())
        self.assertEqual(cm.exception.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(cm.exception.detail, "File has been rejected (there are already 99 files)")

    def test_get_files_non_empty(self):
        # test getting files when the load_files list is not empty
        files = [
            {"id": "1", "name": "test1.txt", "url": "http://99files.com/file1"},
            {"id": "2", "name": "test2.txt", "url": "http://99files.com/file2"},
            {"id": "3", "name": "test3.txt", "url": "http://99files.com/file3"}
        ]
        self.service.load_files = files
        response = self.service.get_files()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_files_empty(self):
        # test getting files when the load_files list is empty
        response = self.service.get_files()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_file_id_found(self):
        # test getting a file by id when it exists
        files = [
            {"id": "1", "name": "test1.txt", "url": "http://99files.com/file1"},
            {"id": "2", "name": "test2.txt", "url": "http://99files.com/file2"},
            {"id": "3", "name": "test3.txt", "url": "http://99files.com/file3"}
        ]
        self.service.load_files = files
        id_file = "2"
        response = self.service.get_file_id(id_file)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_file_id_not_found(self):
        # test getting a file by id when it exists
        files = [
            {"id": "1", "name": "test1.txt", "url": "http://99files.com/file1"},
            {"id": "2", "name": "test2.txt", "url": "http://99files.com/file2"},
            {"id": "3", "name": "test3.txt", "url": "http://99files.com/file3"}
        ]
        self.service.load_files = files
        id_file = "4"
        with self.assertRaises(HTTPException) as context:
            self.service.get_file_id(id_file)
        self.assertEqual(context.exception.status_code, status.HTTP_404_NOT_FOUND)


if __name__ == '__main__':
    unittest.main()
