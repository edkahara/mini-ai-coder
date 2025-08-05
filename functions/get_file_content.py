import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        full_path = os.path.join(working_directory, file_path)
        absolute_path = os.path.abspath(full_path)
        cwd_absolute_path = os.path.abspath(working_directory)

        if not absolute_path.startswith(cwd_absolute_path):
            error = f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
            print(error)
            return error

        is_file = os.path.isfile(absolute_path)
        if not is_file:
            error = f'Error: File not found or is not a regular file: "{file_path}"'
            print(error)
            return error

        with open(absolute_path, "r") as f:
            stripped = f.read().strip()
            split_up = stripped.split()
            len_chars = sum(len(word) for word in split_up)
            result = f'{stripped[:MAX_CHARS]}\n[...File "{file_path}" truncated at 10000 characters]' if len_chars > 10000 else stripped
            print(result)
            return result
    except:
        error = f'Error: An error occured'
        print(error)
        return error

# if __name__ == "__main__":
#     get_file_content("calculator", "main.py")
