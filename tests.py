import unittest
from functions.get_files_info import get_files_info

class Tests(unittest.TestCase):
    def setUp(self):
        self.get_files_info = get_files_info

    def test_current_directory(self):
        result = self.get_files_info("calculator",".")
        test = "Result for current directory:\n- tests.py: file_size=1330 bytes, is_dir=False\n- main.py: file_size=564 bytes, is_dir=False\n- pkg: file_size=128 bytes, is_dir=True"
        self.assertEqual(result, test)

    def test_pkg_directory(self):
        result = self.get_files_info("calculator","pkg")
        test = "Result for 'pkg' directory:\n- render.py: file_size=753 bytes, is_dir=False\n- calculator.py: file_size=1720 bytes, is_dir=False"
        self.assertEqual(result, test)
    
    def test_bin_directory(self):
        result = self.get_files_info("calculator","/bin")
        test = "Result for '/bin' directory:\n\tError: Cannot list '/bin' as it is outside the permitted working directory"
        self.assertEqual(result, test)

    def test_up_one_dir_directory(self):
        result = self.get_files_info("calculator","../")
        test = "Result for '../' directory:\n\tError: Cannot list '../' as it is outside the permitted working directory"
        self.assertEqual(result, test)


if __name__ == "__main__":
    unittest.main()