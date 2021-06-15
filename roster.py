import csv
import collections
from txt_reader import TXT_Reader


class Roster:
    roster_txt = ""
    first_names = []
    last_names = []
    net_IDs = []
    total_numbers = 0
    start = 0


    def __init__(self, filename):
        self.roster_txt = TXT_Reader(filename)
        self.extract_all()
    

    def has_next(self)->bool:
        return self.start < self.total_numbers
    

    def read_next()->list:
        res = []
    

    def set_to(self, num)->None:
        if num >= self.total_numbers:
            self.start = num
        self.start = num


    def extract_all(self)->None:
        while not self.roster_txt.is_end():
            self.extract_one()


    def extract_one(self)->None:
        line = self.roster_txt.read_line()
        if not line or len(line) == 0:
            return
        self.first_names.append(self.extract_firstname(line))
        self.last_names.append(self.extract_lastname(line))
        self.net_IDs.append(self.extract_ID(line))
        self.total_numbers += 1


    def extract_lastname(self, line)->str:
        result = []
        idx = 0
        while idx < len(line):
            if str(line[idx]).isalpha():
                for i in range(idx, len(line)):
                    if line[i] == ',': break
                    result.append(line[i])
                break
            else:
                idx+=1
                continue
        return ('').join(result)    


    def extract_firstname(self, line)->str:
        result = []
        idx = 0
        while idx < len(line):
            if line[idx] == ' ' and line[idx-1] == ',':
                for i in range(idx+1, len(line)):
                    if line[i] == ' ' and line[i+1] == '(': break
                    result.append(line[i])
                break
            else:
                idx+=1
                continue
        return ('').join(result)
    

    def extract_ID(self, line)->str:
        result = []
        idx = 0
        while idx < len(line):
            if line[idx] != '(':
                idx+=1
                continue
            else:
                for i in range(idx+1, len(line)):
                    if (line[i] == ')'): break
                    result.append(line[i])
                break
        return ('').join(result)


    def size(self)->int:
        return self.total_numbers


"""Define execuatables"""
def main():
    r = Roster("assets/roster.txt")
    print(r.first_names)
    print(r.last_names)
    print(r.net_IDs)


if __name__ == "__main__":
    main()

    
    