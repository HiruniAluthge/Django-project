import csv

from interview_project import interview_project

def read_csv_file(file_path):
        data = []
        with open(file_path, 'r') as csv_file:
             csv_reader = csv.reader(csv_file)
             next(csv_reader, None)
             for row in csv_reader:
                  data.append({
                    'col1': row[0],
                    'col2': row[1],
                    'col3': row[2],
                # Add more columns as needed based on your CSV structure
             })
        return data

def main():
    csv_files = ['Ganison_dataset_1.csv', 'Ganison_dataset_2.csv', 'ganison_dataset_3.csv', 'ganison_dataset_4.csv', 'ganison_dataset_5.csv', 'ganison_dataset_6.csv']
    all_csv_data = {}

    for csv_file in csv_files:
        csv_data = read_csv_file(csv_file)
        all_csv_data[csv_file] = csv_data