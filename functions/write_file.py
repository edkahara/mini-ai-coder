import os    

def write_file(working_directory, file_path, content):
    try:
        full_path = os.path.join(working_directory, file_path)
        absolute_path = os.path.abspath(full_path)
        cwd_absolute_path = os.path.abspath(working_directory)

        if not absolute_path.startswith(cwd_absolute_path):
            error = f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
            print(error)
            return error

        with open(absolute_path, "w") as f:
            f.write(content)
            success_message = f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
            print(success_message)
            return success_message
            
    except:
        error = f'Error: An error occured'
        print(error)
        return error

# if __name__ == "__main__":
#     write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
