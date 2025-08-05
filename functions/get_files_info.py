import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    dir_name = 'current' if directory == '.' else f"'{directory}'"
    header = f"Result for {dir_name} directory:"

    full_path = os.path.join(working_directory, directory)
    absolute_path = os.path.abspath(full_path)
    cwd_absolute_path = os.path.abspath(working_directory)

    if not absolute_path.startswith(cwd_absolute_path):
        error = f"{header}\n\tError: Cannot list '{directory}' as it is outside the permitted working directory"
        print(error)
        return error
    if not os.path.isdir(absolute_path):
        error = f"{header}\n\tError: '{directory}' is not a directory"
        print(error)
        return error

    contents = [header]
    for item in os.listdir(absolute_path):
        is_file = os.path.isfile(os.path.join(absolute_path, item))
        size = os.path.getsize(os.path.join(absolute_path, item))
        contents.append(f"- {item}: file_size={size} bytes, is_dir={not is_file}")

    result = "\n".join(contents)
    print(result)
    return result

# if __name__ == "__main__":
#     get_files_info("calculator",".")

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)