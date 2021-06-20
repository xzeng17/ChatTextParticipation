from txt_reader import TXT_Reader


class Roster:


    def __init__(self, filename):
        self.roster_txt = TXT_Reader(filename)
        self.first_names = []
        self.last_names = []
        self.net_IDs = []
        self.UIDS = []
        self.emails = []
        self.universities = []
        self.indexes = {}   #{Full name: int}   ex: {Xuankun Zeng: 15}
        self.total_numbers = 0
        self.start = 0
        self.extract_all()
    

    def has_next(self)->bool:
        return self.start < self.total_numbers
    

    def read_next(self)->list:
        res = []    # Last Name, First Name, NetID
        res.append(self.last_names[self.start])
        res.append(self.first_names[self.start])
        res.append(self.net_IDs[self.start])
        res.append(self.UIDS[self.start])

        self.start += 1
        return res

    
    def read_all(self)->list:
        res = [] # [[]]
        while self.has_next():
            res.append(self.read_next())
        return res


    def set_to(self, num)->None:
        if num >= self.total_numbers:
            self.start = num
        self.start = num


    def extract_all(self)->None:
        while self.roster_txt.has_next():
            self.extract_one()


    def extract_one(self)->None:
        line = self.roster_txt.read_line()
        if not line or len(line) == 0:
            return
        line_list = line.split('\t')
        if not line_list or len(line_list) < 6:
            return
        full_name = line_list[5]
        first_name = full_name.split(',')[1][1:]
        last_name = full_name.split(',')[0]

        self.first_names.append(first_name)
        self.last_names.append(last_name)
        self.net_IDs.append(line_list[2])
        self.universities.append(line_list[3])
        self.UIDS.append(line_list[4])
        self.emails.append(line_list[6][0:len(line_list[6])-1])
        
        self.total_numbers += 1


    def size(self)->int:
        return self.total_numbers


"""Executables"""
def main():
    r = Roster("assets/roster.txt")
    print(r.last_names)


if __name__ == "__main__":
    main()

    
    