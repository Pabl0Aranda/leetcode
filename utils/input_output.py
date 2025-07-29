def read_input(path):
    with open(path, 'r') as file:
        return file.read()

def write_output(path, data):
    with open(path, 'w') as file:
        file.write(str(data))