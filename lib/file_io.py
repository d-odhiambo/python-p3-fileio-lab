def write_file(file_name, file_content):
    """Write content to a .txt file. (overwrites if file exists)"""
    with open(f"{file_name}.txt", "w") as file:
        file.write(file_content)

def append_file(file_name, append_content):
    """Appends content to a .txt file. (creates file if it doesn't exist)"""
    with open(f"{file_name}.txt", "a") as file:
        file.write(append_content)

def read_file(file_name):
    """Reads content from a .txt file and returns it as a string."""
    with open(f"{file_name}.txt", "r") as file:
        return file.read()
