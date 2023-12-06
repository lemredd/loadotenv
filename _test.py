import os
import unittest

from main import load_env


class CoreFunctionalityTestCase(unittest.TestCase):
    def setUp(self):
        self.FILE_LOC = "./.env_fixture"

        lines = """
# This is a comment
foo=bar
        """

        with open(self.FILE_LOC, mode="w") as test_file:
            test_file.write(lines)

    def test_loading_of_environment_vars(self):
        load_env(self.FILE_LOC)
        self.assertEqual(os.environ["foo"], "bar")

    def tearDown(self):
        os.remove(self.FILE_LOC)


class EdgeCasesTestCase(unittest.TestCase):
    def setUp(self):
        self.FILE_LOC = "./.env_fixture"

        self.lines = """
# This is a comment
invalid===var1
        """

        with open(self.FILE_LOC, mode="w") as test_file:
            test_file.write(self.lines)

    def test_erroneous_lines(self):
        with self.assertRaises(AttributeError):
            load_env(self.FILE_LOC)

    def tearDown(self):
        os.remove(self.FILE_LOC)


if __name__ == '__main__':
    unittest.main()
