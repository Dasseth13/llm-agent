import os

def get_files_info(working_directory: str, directory: str=".") -> str:
    abs_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(abs_path, directory))

    valid_dir = os.path.commonpath([abs_path, target_dir]) == abs_path
    if not valid_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(target_dir):
        return f'Error: "{directory} is not a directory"'

    print(target_dir)
    target_files_list: list[str] = os.listdir(target_dir)

    str_list = []
    for file in target_files_list:
        full_filepath = target_dir + "/" + file
        file_size: int = os.path.getsize(full_filepath)
        is_dir = os.path.isdir(full_filepath)
        file_str = f"  - {file}: file_size={file_size} bytes, is_dir={is_dir}"
        str_list.append(file_str)

    final_str = "Result for current directory:\n" + "\n".join(str_list)
    return final_str
