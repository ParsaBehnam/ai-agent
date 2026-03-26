import os
import subprocess
def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))

        if os.path.commonpath([working_dir_abs, file_path_abs]) != working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file_path_abs):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path_abs.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", file_path_abs]
        if args != None:
            command.extend(args)

        result = subprocess.run(command,            # returns a CompletedProcess obj
                                cwd=working_dir_abs,
                                capture_output= True,
                                text=True,
                                timeout=30)
        output_string = ''

        if result.returncode != 0:
            output_string += f'Process exited with code {result.returncode}'
        if not len(result.stdout) and not len(result.stderr):
            output_string += "No output produced"

        if result.stdout:
            output_string += f'STDOUT: {result.stdout}'
        if result.stderr:
            output_string += f'STDERR: {result.stderr}'
        
        return output_string


    except Exception as e:
        return f"Error: executing Python file: {e}"
