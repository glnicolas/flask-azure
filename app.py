from flask import Flask
import csv
app = Flask(__name__)

name = 'Nico'

@app.route("/")
def hello():
    return "Welcome! "+name

@app.route("/open-csv")
def openCsv():
    data = ""
    with open('GetSubscriptions.csv',encoding ="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                #print(f'\t{row}')
                data+= f'\t{row}'
                line_count += 1
        print(f'Processed {line_count} lines.')
    return data

