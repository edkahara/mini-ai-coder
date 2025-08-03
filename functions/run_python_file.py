import os  
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    try:
        full_path = os.path.join(working_directory, file_path)
        absolute_path = os.path.abspath(full_path)
        cwd_absolute_path = os.path.abspath(working_directory)

        if not absolute_path.startswith(cwd_absolute_path):
            error = f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
            print(error)
            return error

        is_file = os.path.isfile(absolute_path)
        if not is_file:
            error = f'Error: File "{file_path}" not found.'
            print(error)
            return error

        if not file_path.endswith(".py"):
            error = f'Error: "{file_path}" is not a Python file.'
            print(error)
            return error

        response = subprocess.run(["python", absolute_path] + args, capture_output=True,timeout=30)
        result = None
        if response.returncode != 0:
            result = f'Process exited with code {response.returncode}'
        elif response.stdout:
            result = 'STDOUT:' + response.stdout.decode("utf-8")
        else:
            result = 'No output produced.'
        
        print(result)
        return result
    except subprocess.CalledProcessError as e:
        error = f"Error: executing Python file: {e}"
        print(error)
        return error
    except:
        error = f'Error: An error occured'
        print(error)
        return error

# if __name__ == "__main__":
#     run_python_file("calculator", "tests.py")
