import csv

class Timeline:
    def __init__(self):
        self.data = None
        self.title = None

    def read(self, path):
        self.data = {}

        with open(path, 'r') as data_file:
            for row in csv.reader(data_file):

                # Logic to assign each row as either periods or events
                # in data structure.
                if row[2] != None or row[2] != 0:
                    data[row[0]] = (row[1], row[2])
                else:
                    data[row[0]] = row[1]
