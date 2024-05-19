#!/usr/bin/python3
import inspect
import pep8


class TestClassDocumentation():

    def __init__(self, tests, _class):
        self.tests = tests
        self.name = _class

        # Get all the methods of class @name
        self.functions = inspect.getmembers(self.name, inspect.isfunction)

    def documentation(self):
        with self.tests.subTest(msg='Testing methods'):
            for f in self.functions:
                with self.tests.subTest(msg='Documentation method {}'
                                        .format(f[0])):

                    doc = f[1].__doc__
                    self.tests.assertGreaterEqual(len(doc), 1)

        with self.tests.subTest(msg='Testing class'):
            doc = self.name.__doc__
            self.tests.assertGreaterEqual(len(doc), 1)

    def pep8(self, files):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(files)
        self.tests.assertEqual(result.total_errors, 0,
                               'Found code style errors (and warnings)."')

if __name__ == '__main__':
    unittest.main()