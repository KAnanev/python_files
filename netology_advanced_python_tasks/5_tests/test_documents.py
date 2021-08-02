import app
import unittest
from unittest.mock import patch


class TestMainDocuments(unittest.TestCase):
    def setUp(self) -> None:
        with patch('app.input', return_value='q'):
            app.secretary_program_start()


    def test_get_real_doc_shelf(self):
        with patch('app.input') as in_mock:
            in_mock.return_value = '11-2'

            doc_name = app.get_doc_shelf()
            self.assertEqual('1', doc_name)

    def test_not_get_wrong_doc_shelf(self):
        with patch('app.input') as in_mock:
            in_mock.return_value = '10006'

            doc_name = app.get_doc_shelf()
            self.assertNotEqual('1', doc_name)

            in_mock.return_value = '12345'
            doc_name = app.get_doc_shelf()
            self.assertIsNone(doc_name)

class TestClassDoc(unittest.TestCase):
    def setUp(self) -> None:
        self.dirs, self.docs = app.update_date()
        self.app = app.Directories(self.dirs, self.docs)

    def test_get_document(self):
        doc = self.app.get_documents('123')
        test_add = {"type": "test_type", "number": "123", "name": "test_uset"}
        self.assertDictEqual(doc, test_add)