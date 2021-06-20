from txt_reader import TXT_Reader
from inspect import currentframe, getframeinfo
from roster import Roster

class Chat:
    # input_file
    #valid_chats = []   # [[]]   [zoom_name, time]
    """attendance records who should recieve full point for discussion attendance point"""
    #attendance = set([])     # {Last_name + " " + first three letter of First_name} 
    #check_points = []   #[[start time, end time], [start time, end time], ...]
    #attendance_temp = {}    # {zoom_name: [] <- (length of check_points)}

    def __init__(self, filename, roster):
        self.valid_chats = []
        self.attendance = set([])
        self.check_points = []
        self.attendance_temp = {}
        self.roster = roster

        self.input_file = TXT_Reader(filename)
        self.process_all()
        self.input_file.close()
        self.take_attendance()


    def is_present(self, key)->bool:
        return key in self.attendance


    def take_attendance(self)->None:
        for chat in self.valid_chats:
            name = chat[0]
            time = chat[1]
            for i in range (0, len(self.check_points)):
                check_point = self.check_points[i]
                if self.in_range(time, check_point):
                    if name not in self.attendance_temp:
                        self.attendance_temp[name] = [0] * len(self.check_points)
                    self.attendance_temp[name][i] = 1
        
        for key, value in self.attendance_temp.items():
            checks = 0
            for ele in value:
                if ele == 1:
                    checks += 1
            if checks >= len(self.check_points)-1:
                self.attendance.add(self.edit_name(key))    # refine name
        return


    def edit_name(self, zoom_name)->str:
        if self.is_email(zoom_name):
            i = 0
            while zoom_name[i] != '@':
                i+=1
            net_id = zoom_name[:i]
            i = self.roster.net_IDs.index(net_id)
            zoom_name = self.roster.first_names[i]+" "+self.roster.last_names[i]
            

        last_name = ""
        first_name_3_letter = [" ", " ", " "]

        zoom_name = zoom_name.split(" ")

        # extract last name
        for i in range(len(zoom_name)-1, -1, -1):
            if zoom_name[i][0] == "(":
                continue
            last_name = zoom_name[i]
            break
        
        # extract first name
        for i in range(0, 3):
            if i >= len(zoom_name[0]): break
            first_name_3_letter[i] = zoom_name[0][i]

        return last_name+" "+("").join(first_name_3_letter)


    def process_all(self)->None:
        while (self.input_file.has_next()):
            line = self.input_file.read_line()
            
            if not self.valid_line(line):
                continue
            
            converted_time = self.convert_time(self.extract_time(line))
            if self.is_start(line):
                time_range = [converted_time, converted_time+30]
                self.insert_intervals(time_range)
            elif self.is_stop(line):
                time_range = [converted_time-30, converted_time]
                self.insert_intervals(time_range)
            else:
                self.valid_chats.append([self.extract_zoom_name(line), converted_time])
    

    def insert_intervals(self, new_interval)->None:
        # insert the new_interval into self.check_points, new_interval's begin time 
        # if there is an overlap, merge
        # else append the new interval
        # self.check_points is sorted by first element in the pair in increasing order
        for interval in self.check_points:
            if self.overlapped(interval, new_interval):
                interval[0] = min(interval[0], new_interval[0])
                interval[1] = max(interval[1], new_interval[1])
                return
        self.check_points.append(new_interval)
        return


    def overlapped(self, lhs, rhs)->bool:
        # assume lhs[0] <= rhs[0] and lhs[0] <= lhs[1] and rhs[0] <= rhs[1]
        if (lhs[0] > rhs[0]): return self.overlapped(rhs, lhs)
        if lhs[1] < rhs[0]: return False
        return True
    
    
    def valid_line(self, line)->bool:
        if len(line) < 14:
            return False
        if line[2] != ':' or line[5] != ':':
            return False
        if not (self.is_number(line[0:2]) and self.is_number(line[3:5]) and self.is_number(line[6:8])):
            return False
        if line[9:13] != "From":
            return False
        return True


    def is_number(self, string)->bool:
        return string.isdigit()


    def extract_time(self, line)->str:  # hh:mm:ss
        return line[0:8]


    def extract_zoom_name(self, line)->str:
        l = 14
        r = len(line)-1
        while not str(line[l]).isalpha():
            l += 1
        
        r = l

        while line[r] != ' ' or line[r:r+4] != ' to ':
            r += 1
        
        while l < r and line[r] == ' ':
            r -= 1
        return line[l:r+1]


    def convert_time(self, extracted_time)->int:
        # input extracted_time: "14:29:59"
        hh = extracted_time[0:2]
        mm = extracted_time[3:5]
        ss = extracted_time[6:8]
        return int(ss)+60*int(mm)+60*60*int(hh)

    
    def is_start(self, line)->bool:
        if self.extract_zoom_name(line) != "Brad Mehrtens": return False
        last_word = line.split(" ")[-1]
        candidate = "START"
        matches = 0
        idx = 0
        while idx < len(candidate) and idx < len(last_word):
            if candidate[idx].lower() == last_word[idx].lower():
                matches += 1
            idx += 1
        return matches/len(candidate) > 0.75


    def is_stop(self, line)->bool:
        if self.extract_zoom_name(line) != "Brad Mehrtens": return False
        last_word = line.split(" ")[-1]
        candidate = "STOP"
        matches = 0
        idx = 0
        while idx < len(candidate) and idx < len(last_word):
            if candidate[idx].lower() == last_word[idx].lower():
                matches += 1
            idx += 1
        return matches/len(candidate) > 0.75


    def is_email(self, zoom_name)->bool:
        return '@' in zoom_name


    def in_range(self, time, interval)->bool:
        return interval[0] <= time <= interval[1]


"""Executables"""
def main():
    roster = Roster("assets/roster.txt")
    chatone = Chat("input/chat_week1_2.txt", roster)
    chattwo = Chat("input/chat_week1_1.txt", roster)
    print(chatone.attendance)
    print(len(chatone.attendance))
    print(chattwo.attendance)
    print(len(chattwo.attendance))

if __name__ == "__main__":
    main()
