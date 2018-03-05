import csv
import os

def save_data_to_csv(file_name, header, data):
    if not os.path.isdir(''.join(['../output'])):
        os.makedirs(''.join(['../output']))

    output_file = open(''.join(['../output/', file_name, '.csv']), 'w')

    with output_file:
        output_writer = csv.writer(output_file, delimiter=',')
        output_writer.writerow(header)
        for row in data:
            output_writer.writerow(row)

