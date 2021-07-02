from concept_question import Concept_question
from roster import Roster
from csv_file import CSV
from chat import Chat
import os
import shutil
import sys

def main():
    args = sys.argv[1:]

    # constants path/file names
    cq_filename = "output/concept_question_grades_SUM2021.csv"
    chat_filename = "output/chat_grades_SUM2021.csv"
    input_path = "input/"
    roster = Roster("assets/roster.txt")

    if args and args[0] == "init":
        # init names from roster
        # output csv file with only names and Ids
        
        csv_file = CSV()

        csv_file.fields = ["Last Name", "First Name", "NetID", "UID"]
        csv_file.entries = roster.read_all()

        csv_file.write_to_file_plain("output/init.csv")
        return

    if args and args[0] == "update":
        # update chat_grades and concept_question_grades entries with new roster file
        chat_grades = CSV()
        concept_question_grades = CSV()
        chat_grades.read_from_file(chat_filename)               # old file
        concept_question_grades.read_from_file(cq_filename)     # old file

        new_chat = CSV()        # updated file
        new_concept = CSV()     # updated file

        new_chat.fields = chat_grades.fields
        new_concept.fields = concept_question_grades.fields

        for entry in chat_grades.entries:
            UID = entry[3]
            if roster.has_UID(UID):
                new_chat.entries.append(entry)
        
        for entry in concept_question_grades.entries:
            UID = entry[3]
            if roster.has_UID(UID):
                new_concept.entries.append(entry)

        new_chat.write_to_file_plain(chat_filename)     # replace old file
        new_concept.write_to_file_plain(cq_filename)    # replace old file
        return

    ########################################################################################
    #                         filename required after this line                            #
    ########################################################################################

    filename = args[1]

    if args and args[0] == "chat":
        # take Friday discussion's attendance
        # always have two input file
        if len(args) < 3:
            print("Error: Must have input files for both Discussions!")
        filename2 = args[2]
        print(filename)
        print(filename2)
        chat1 = Chat(input_path+filename, roster)
        chat2 = Chat(input_path+filename2, roster)
        csv_file = CSV()
        csv_file.read_from_file(chat_filename)

        # add discussion number in fields
        discussion_num = 1
        previous_num = csv_file.fields[-1]
        if previous_num.isdigit():
            discussion_num += int(previous_num)
        csv_file.append_fields(discussion_num)

        for entry in csv_file.entries:
            last_name = entry[0].split(' ')[0]
            first_name = entry[1]
            
            if len(first_name) > 3:
                first_name = first_name[0:3]
            else:
                first_name = first_name + " "*(3-len(first_name))
            key = last_name+" "+first_name

            if chat1.is_present(key) or chat2.is_present(key):
                entry.append("10")
            else:
                entry.append("0")
        csv_file.write_to_file_plain(chat_filename)

        shutil.move(input_path+filename, input_path+"finished_chat/"+filename)
        shutil.move(input_path+filename2, input_path+"finished_chat/"+filename2)
    
    if args and args[0] == "cq":
        # append the concept question grades to a target file
        cq = Concept_question(input_path+filename)
        csv_file = CSV()
        csv_file.read_from_file(cq_filename)
        csv_file.append_fields(cq.title)
        csv_file.add_all_cqs(cq.grades)
        csv_file.write_to_file_plain(cq_filename)

        shutil.move(input_path+filename, input_path+"finished_cq/"+filename)

    if not args:
        print("No action taken")


if __name__ == "__main__":
    main()