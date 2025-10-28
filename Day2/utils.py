
def read_text(file_path):
    """Reads a text file and returns list of lines"""
    with open(file_path, 'r') as f:
        return f.readlines()

def write_text(file_path, lines_list):
    """Writes list of strings to a text file"""
    with open(file_path, 'w') as f:
        for line in lines_list:
            f.write(line)
