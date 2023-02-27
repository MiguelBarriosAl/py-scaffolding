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


if __name__ == '__main__':
    unittest.main()
