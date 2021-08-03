class Open_File:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with Open_File('topCPU.txt.py', 'r') as f:
    a = f.readlines()
    for lines in a:
        if len(lines) > 2 and len(lines) < 20:
            print('the percentage is ' + lines)
        elif len(lines) > 20:
            print('the date is ' + lines)








