from roster import Roster
from csv_file import CSV

def main():

    # init names from roster
    roster = Roster("assets/roster.txt")
    csv_file = CSV()

    csv_file.fields = ["Last Name", "First Name", "NetID"]
    csv_file.entries = roster.read_all()

    csv_file.write_to_file_plain("output/init.csv")
    return


if __name__ == "__main__":
    main()