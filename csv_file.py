import csv


class CSV:
    input_name = "output/test.csv"
    output_name = "output/test2.csv"
    fields = []
    entries = []    #[[]]   Last name, First name, NetID, UID, discussion 1, discussion 2...

    
    def read_from_file(self, filename):
        with open(filename, 'r', newline='') as input_file:
            spamreader = csv.reader(input_file)
            line_number = 0
            for row in spamreader:
                if line_number == 0:
                    self.fields = row
                else:
                    self.entries.append(row)
                line_number+=1


    # not going to use
    def write_to_file_dict(self, filename):
        with open(filename, 'w+', newline='') as output_file:
            fields = self.fields
            writer = csv.DictWriter(output_file, fieldnames=fields)
            writer.writeheader()
            for row in self.entries:
                row_data = {}
                for i in range(0, len(fields)):
                    row_data[fields[i]] = row[i]
                writer.writerow(row_data)
        print("File saved -> "+filename)
    

    def write_to_file_plain(self, filename):
        with open(filename, 'w+', newline='') as output_file:
            fields = self.fields
            writer = csv.writer(output_file)
            
            writer.writerow(fields)         # write header
            writer.writerows(self.entries)  # write entries
        print("File saved -> "+filename)


    def append_fields(self, field):
        self.fields.append(field)
    
    def add_all_cqs(self, cq_db):   # cq_db is a dict reference to the class instance of Concept_question object
        for entry in self.entries:
            net_id = entry[2]
            if (net_id in cq_db):
                entry.append(cq_db[net_id])
            else:
                entry.append(0)



"""Execatables"""
def main():
    file = CSV()
    file.read_from_file(file.input_name)
    file.write_to_file_plain(file.output_name)

if __name__ == "__main__":
    main()
