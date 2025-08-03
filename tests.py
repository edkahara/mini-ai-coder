import unittest
# from functions.get_files_info import get_files_info
# from functions.get_file_content import get_file_content
# from functions.write_file import write_file
from functions.run_python_file import run_python_file

# class Tests(unittest.TestCase):
#     def setUp(self):
#         self.get_files_info = get_files_info

#     def test_current_directory(self):
#         result = self.get_files_info("calculator",".")
#         test = "Result for current directory:\n- tests.py: file_size=1330 bytes, is_dir=False\n- main.py: file_size=564 bytes, is_dir=False\n- pkg: file_size=128 bytes, is_dir=True"
#         self.assertEqual(result, test)

#     def test_pkg_directory(self):
#         result = self.get_files_info("calculator","pkg")
#         test = "Result for 'pkg' directory:\n- render.py: file_size=753 bytes, is_dir=False\n- calculator.py: file_size=1720 bytes, is_dir=False"
#         self.assertEqual(result, test)
    
#     def test_bin_directory(self):
#         result = self.get_files_info("calculator","/bin")
#         test = "Result for '/bin' directory:\n\tError: Cannot list '/bin' as it is outside the permitted working directory"
#         self.assertEqual(result, test)

#     def test_up_one_dir_directory(self):
#         result = self.get_files_info("calculator","../")
#         test = "Result for '../' directory:\n\tError: Cannot list '../' as it is outside the permitted working directory"
#         self.assertEqual(result, test)

# class Tests(unittest.TestCase):
#     def setUp(self):
#         self.get_file_content = get_file_content

#     def test_calculator_main(self):
#         result = self.get_file_content("calculator","main.py")
#         test = """import sys
# from pkg.calculator import Calculator
# from pkg.render import render


# def main():
#     calculator = Calculator()
#     if len(sys.argv) <= 1:
#         print("Calculator App")
#         print('Usage: python main.py "<expression>"')
#         print('Example: python main.py "3 + 5"')
#         return

#     expression = " ".join(sys.argv[1:])
#     try:
#         result = calculator.evaluate(expression)
#         to_print = render(expression, result)
#         print(to_print)
#     except Exception as e:
#         print(f"Error: {e}")


# if __name__ == "__main__":
#     main()"""
#         self.assertEqual(result, test)

#     def test_pkg_directory(self):
#         result = self.get_file_content("calculator","pkg/calculator.py")
#         test = """class Calculator:
#     def __init__(self):
#         self.operators = {
#             "+": lambda a, b: a + b,
#             "-": lambda a, b: a - b,
#             "*": lambda a, b: a * b,
#             "/": lambda a, b: a / b,
#         }
#         self.precedence = {
#             "+": 1,
#             "-": 1,
#             "*": 2,
#             "/": 2,
#         }

#     def evaluate(self, expression):
#         if not expression or expression.isspace():
#             return None
#         tokens = expression.strip().split()
#         return self._evaluate_infix(tokens)

#     def _evaluate_infix(self, tokens):
#         values = []
#         operators = []

#         for token in tokens:
#             if token in self.operators:
#                 while (
#                     operators
#                     and operators[-1] in self.operators
#                     and self.precedence[operators[-1]] >= self.precedence[token]
#                 ):
#                     self._apply_operator(operators, values)
#                 operators.append(token)
#             else:
#                 try:
#                     values.append(float(token))
#                 except ValueError:
#                     raise ValueError(f"invalid token: {token}")

#         while operators:
#             self._apply_operator(operators, values)

#         if len(values) != 1:
#             raise ValueError("invalid expression")

#         return values[0]

#     def _apply_operator(self, operators, values):
#         if not operators:
#             return

#         operator = operators.pop()
#         if len(values) < 2:
#             raise ValueError(f"not enough operands for operator {operator}")

#         b = values.pop()
#         a = values.pop()
#         values.append(self.operators[operator](a, b))"""
#         self.assertEqual(result, test)
    
#     def test_bin_directory(self):
#         result = self.get_file_content("calculator","/bin/cat")
#         test = 'Error: Cannot list "/bin/cat" as it is outside the permitted working directory'
#         self.assertEqual(result, test)

#     def test_file_not_found(self):
#         result = self.get_file_content("calculator","pkg/does_not_exist.py")
#         test = 'Error: File not found or is not a regular file: "pkg/does_not_exist.py"'
#         self.assertEqual(result, test)

# class Tests(unittest.TestCase):
#     def setUp(self):
#         self.write_file = write_file
    
#     def test_lorem(self):
#         result = self.write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
#         test = 'Successfully wrote to "lorem.txt" (28 characters written)'
#         self.assertEqual(result, test)

#     def test_morelorem(self):
#         result = self.write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
#         test = 'Successfully wrote to "pkg/morelorem.txt" (26 characters written)'
#         self.assertEqual(result, test)

#     def test_not_allowed(self):
#         result = self.write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
#         test = 'Error: Cannot write to "/tmp/temp.txt" as it is outside the permitted working directory'
#         self.assertEqual(result, test)


# if __name__ == "__main__":
#     unittest.main()

class Tests(unittest.TestCase):
    def setUp(self):
        self.run_python_file = run_python_file
    
    def test_calc_instructions(self):
        result = self.run_python_file("calculator", "main.py")
        test = '''STDOUT:
Calculator App
Usage: python main.py "<expression>"
Example: python main.py "3 + 5"
'''
        self.assertEqual(result, test)

    def test_calculate(self):
        result = self.run_python_file("calculator", "main.py", ["3 + 5"])
        test = '''STDOUT:
┌─────────┐
│  3 + 5  │
│         │
│  =      │
│         │
│  8      │
└─────────┘
'''
        self.assertEqual(result, test)

    def test_calculator_tests(self):
        result = self.run_python_file("calculator", "tests.py")
        test = '''STDERR:
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
'''
        self.assertEqual(result, test)

    def test_invalid_dir(self):
        result = self.run_python_file("calculator", "../main.py")
        test = 'Error: Cannot execute "../main.py" as it is outside the permitted working directory'
        self.assertEqual(result, test)

    def test_nonexistent(self):
        result = self.run_python_file("calculator", "nonexistent.py")
        test = 'Error: File "nonexistent.py" not found.'
        self.assertEqual(result, test)


if __name__ == "__main__":
    unittest.main()