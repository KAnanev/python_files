# main.py is required only for repl.it

import unittest
from tests import test_app, test_example 

def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    tests1 = loader.loadTestsFromModule(test_app)
    tests2 = loader.loadTestsFromModule(test_example)
    suite.addTests(tests1)
    suite.addTests(tests2)
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
