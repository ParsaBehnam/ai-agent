import os

def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs # True / False
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        items_record_list = []
        for item in os.listdir(target_dir):
            full_path = os.path.join(target_dir, item)
            items_record_list.append(f'- {item}: file_size={os.path.getsize(full_path)}, is_dir={os.path.isdir(full_path)}')
        return '\n'.join(items_record_list)
    except Exception as e:
        return f"Error: {e}"
        
   



