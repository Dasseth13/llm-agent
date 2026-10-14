import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        abs_path = os.path.abspath(working_directory)
        full_file_path = os.path.normpath(os.path.join(abs_path, file_path))
        if os.path.commonpath([abs_path, full_file_path]) != abs_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(full_file_path):
            return f'Error: "{file_path}" does not exist or is not a regualar file'

        if file_path[-3:] != ".py":
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", full_file_path]

        if args is not None:
            command.extend(args)

        process = subprocess.run(command, capture_output=True, check=True, timeout=30, text=True)

        return_string = ""

        if process.returncode != 0:
            return_string += f"Process exited with code {process.returncode}\n"

        if process.stderr is None and process.stdout is None:
            return_string += "No output producted\n"

        return_string += f"STDOUT: {process.stdout}\n STDERR: {process.stderr}"
        return return_string



    except Exception as e:
        print(f'Error: on {file_path}: {e}')
