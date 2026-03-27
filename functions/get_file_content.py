import os
from google.genai import types

from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_directory_abs, file_path))

        if not os.path.commonpath([working_directory_abs, target_file]) == working_directory_abs: 
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(target_file, 'r') as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content_string

    except Exception as e:
        return f'Error: {e}'
    
schema_get_file_content = types.FunctionDeclaration(
    name='get_file_content',
    description="Opens a file that exists in given target directory and reads it's contents."
    , parameters= types.Schema(
        type= types.Type.OBJECT,
        required=['file_path'],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Directory path to the targeted file in order to read it content"
            )
            
        }
    )
)