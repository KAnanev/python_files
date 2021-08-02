import app

import unittest
from unittest.mock import patch


class TestDefApp(unittest.TestCase):
    def setUp(self) -> None:
        with patch('app.input', return_value='q'):
            app.secretary_program_start()
            self.dirs, self.docs = app.update_date()
            self.app = app.Directories(self.dirs, self.docs)

    def test_update_date(self):
        self.assertIsInstance(self.docs, list)
        self.assertIsInstance(self.dirs, dict)

    def test_check_document_existance(self):
        doc_ex = app.check_document_existance('11-2')
        self.assertEqual(doc_ex, True)
        doc_ex = app.check_document_existance('0')
        self.assertEqual(doc_ex, False)

    def test_get_all_doc_owners_names(self):
        doc_ex = app.get_all_doc_owners_names()
        self.assertIsInstance(doc_ex, set)

    def test_delete_doc(self):
        with patch('app.input', return_value='11-2'):
            doc_ex = app.delete_doc()
            self.assertEqual(doc_ex[0], '11-2')
        with patch('app.input', return_value='0'):
            self.assertRaises(TypeError)

    def test_add_new_dock(self):
        with patch('app.input', return_value='11-2'):
            doc_ex = app.add_new_doc()
            self.assertEqual(doc_ex, '11-2')


if __name__ == '__main__':
    unittest.runner()
