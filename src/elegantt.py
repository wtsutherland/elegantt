import csv
import sys
import json
import matplotlib.pyplot as plt
import datetime

arg = sys.argv

class Timeline:
    def __init__(self, data_path=None):
        self.data = None
        self.title = None
        self.data  = None

        if data_path:
            self.data = self.read(data_path)
        
        if self.data:
            self.xlimits()

    def read(self, path):
        data = {}

        with open(path, 'r') as data_file:
            for row in csv.reader(data_file):

                # Logic to assign each row as either periods or events
                # in data structure.
                if row[2]:

                    if isinstance(row[2], str):
                        if row[2].lower() == "present":
                            now = datetime.datetime.now()
                            data[row[0]] = (row[1], now)
                    else:
                        data[row[0]] = (row[1], row[2])
                else:
                    data[row[0]] = row[1]

        return data


    def xlimits(self):
        times = []

        for key, value in self.data.items():
            if isinstance(value, str):
                times.append(value)
            elif isinstance(value, tuple):
                times += value

        print(times)
            
        

tm = Timeline(data_path="../tests/test_data.csv")
