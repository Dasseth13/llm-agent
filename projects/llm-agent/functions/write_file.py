import os
import string

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes a given content string to a file with a given file path.  If file does not exist, this creates the file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to write content into, relative to the working directory (default is the working directory itself)",
                },
                "content": {
                    "type": "string",
                    "description": "Content passed into to write into the given file"
                },
            },
        },
    },
}

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        abs_path = os.path.abspath(working_directory)
        full_file_path = os.path.normpath(os.path.join(abs_path, file_path))
        if os.path.commonpath([abs_path, full_file_path]) != abs_path:
            return f'Error: cannot read "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(full_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(file_path, exist_ok=True)

        with open(full_file_path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        print(f'Error: reading file "{file_path}": {e}')
