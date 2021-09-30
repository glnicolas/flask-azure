from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import csv, os
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity

app = Flask(__name__)

name = 'Nico'

table_service = TableService(account_name='ccademployees', account_key='Fvseuyx4DWoFupjqHW5X8fzT3iy3u+7BwtRlK2NDZDGql2uKlv1KNeZu6d9KeYxe1DVdHmwGsnkKNtU8BWMukA==')
#table_service.create_table('tasktable')
task = {'PartitionKey': 'tasksSeattle', 'RowKey': '001',
        'description': 'Take out the trash', 'priority': 200}
#table_service.insert_entity('tasktable', task)

@app.route("/")
def hello():
    return "Welcome! "+name

@app.route("/open-csv")
def openCsv():
    data = "asd"
    with open('/home/uploads/employees.csv',encoding ="utf8") as csv_file:
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

@app.route('/upload')
def upload_view():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join("/home/uploads/", secure_filename(f.filename)))

      return 'file uploaded successfully'
