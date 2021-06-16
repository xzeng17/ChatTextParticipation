
class TXT_Reader:
    file = "a txt file"
    file_name = ""
    lines = []
    
    start = 0
    end = 0


    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(file_name, "r")
        self.__get_lines()
        self.end = len(self.lines)


    # test print document
    def print_line(self):   
        print(self.file.read())


    def has_next(self)->bool:
        return self.start < self.end


    def set_line_to(self, line)->None:
        if (line > self.end):
            self.start = self.end
        else:
            self.start = line


    def read_line(self)->str:
        result = ""
        if self.has_next():
            result = self.lines[self.start]
        self.__next_line()
        return result

    """<----------Private Helper Methods---------->"""
    def __get_lines(self):
        self.lines = self.file.readlines()
    
    def __next_line(self):
        self.start += 1
    

"""Executables"""
def main():
    # tr = TXT_Reader("assets/roster.txt")
    tr = TXT_Reader("input/demo_chat.txt")
    print(tr.lines)


if __name__ == "__main__":
    main()