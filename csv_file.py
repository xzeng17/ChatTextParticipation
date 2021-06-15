import csv
import collections

class CSV:
    input_name = ""
    output_name = "output/test.csv"
    fields = []




    def write_to_file(self, filename):
        with open(filename, 'w+', newline='') as output_file:
            fields = ['Last Name','First Name', 'NetID', 'Lab1']
            writer = csv.DictWriter(output_file, fieldnames=fields)
            writer.writeheader()
        print("File saved -> "+filename)
        

"""Define execuatables"""
def main():
    file = CSV()
    file.write_to_file(file.output_name)

if __name__ == "__main__":
    main()
