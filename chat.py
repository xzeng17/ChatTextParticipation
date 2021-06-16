from txt_reader import TXT_Reader
from inspect import currentframe, getframeinfo

class Chat:

    valid_chats = []   # [[]]   [zoom_name, time]


    def __init__(self, filename):
        self.input_file = TXT_Reader(filename)


    def process_all(self)->None:
        while (self.input_file.has_next()):
            line = self.input_file.read_line()
            if not self.valid_line(line):
                continue
            self.valid_chats.append([self.extract_zoom_name(), self.extract_time()])


    def read_line(self)->str:
        return self.input_file.read_line()

    
    def valid_line(self, line)->bool:
        if len(line) < 14:
            return False
        if line[2] != ':' or line[5] != ':':
            return False
        if not (self.is_number(line[0:2]) and self.is_number(line[3:5]) and self.is_number(line[6:8])):
            return False
        if line[10:14] != "From":
            return False
        return True


    def is_number(self, string)->bool:
        return string.isdigit()


    def extract_time(self, line)->int:  # as minute
        return line[0:9]


    def extract_zoom_name(self, line)->str:
        l = 15
        r = len(line)-1
        while not str(line[l]).isalpha():
            l += 1
        
        r = l

        while line[r+1] != ':':
            r += 1
        
        while l < r and line[r] == ' ':
            r -= 1
        return line[l:r+1]


"""Executables"""
def main():
    chat = Chat("input/demo_chat.txt")
    chat.process_all()

if __name__ == "__main__":
    main()
