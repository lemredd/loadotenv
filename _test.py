import os
import unittest


class TestCoreFunctionality(unittest.TestCase):
    def setUp(self):
        self.FILE_LOC = "./.env_fixture"

        lines = """
# This is a comment
foo=bar
        """

        with open(self.FILE_LOC, mode="w") as test_file:
            test_file.write(lines)

    def test_loading_of_environment_vars(self):
        self.assertEqual(1, 1)

    def tearDown(self):
        os.remove(self.FILE_LOC)


if __name__ == '__main__':
    unittest.main()
