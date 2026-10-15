import os
MAX_CHARS = 10000

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Retrieves the first 10000 characters of a file and indicates if there was a truncation",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to retrieve content from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        abs_path = os.path.abspath(working_directory)
        full_file_path = os.path.normpath(os.path.join(abs_path + "/" + file_path))
        if os.path.commonpath([abs_path, full_file_path]) != abs_path:
            return f'Error: cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(full_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(full_file_path, "r") as f:
            file_content_string: str = f.read(MAX_CHARS)
            if f.read(1) != "":
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return file_content_string

    except Exception as e:
        print(f'Error: reading file "{file_path}": {e}')
