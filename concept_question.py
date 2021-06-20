from txt_reader import TXT_Reader

class Concept_question:
    roster = "" # Roster object
    title = ""
    grades = {} # {uid: str, grade: int}

    def __init__(self, filename):       # filename = "input/T1A.txt"
        self.input_file = TXT_Reader(filename)
        self.title = filename.split("/")[1].split(".")[0]

        self.extract_all_grade()
        self.input_file.close()
    
    def extract_all_grade(self):
        while self.input_file.has_next():
            self.extract_one_grade()

    def extract_one_grade(self):

        prev_line = ""
        cur_line = ""

        IS_NAME_CUE = "View recent activity Help: View_recent_activity Set/Change parameters"
        Net_ID = ""
        IS_GRADE_CUE = "problem weight assigned by computer"
        grade = 0

        # recognize a student name
        # recognizing the next line as IS_NAME_CUE

        while self.input_file.has_next():
            prev_line = cur_line
            cur_line = self.input_file.read_line()
            if cur_line[:69] == IS_NAME_CUE:
                Net_ID = prev_line.split(" ")[-1][1:-2]
                break
        
        while self.input_file.has_next():
            prev_line = cur_line
            cur_line = self.input_file.read_line()
            if cur_line[3:38] == IS_GRADE_CUE:
                grade_str = prev_line[0]
                if (grade_str == "1"):
                    grade = 1
                break
        
        self.grades[Net_ID] = grade


"""Execatables"""
def main():
    cq = Concept_question("input/T1A.txt")
    print("title is: "+cq.title)

    print("Printing dirs")
    print(cq.grades)

    return

if __name__ == "__main__":
    main()
