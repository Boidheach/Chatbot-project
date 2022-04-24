from src.configuration.profile import Profile
import datetime
import json
import os
import xlsxwriter


# Ensures storing/loading/updating of the NeuroSky data
# in the form of a dictionary.
# The data is stored in JSON format.
class NeuroskyDataStorage:
    def __init__(self):
        self.all_data = dict()
        self.clear()

    # Append one sample from all observed variables
    # (keys)
    def append(self, time_elapsed, data):
        for key in data:
            self.all_data[key].append(data[key])
        self.all_data['t'].append(time_elapsed)

    def get_all_data(self):
        return self.all_data

    def save(self):
        # Do not save empty data
        if len(self.all_data['t']) == 0:
            return

        # Create an autogenerated filename
        output_dir = Profile().get_profile()['output_dir']

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        subject_name = Profile().get_profile()['subject_name']
        condition = str(Profile().get_profile()['condition'])
        timestamp = datetime.datetime.now().strftime("%d%m%y_%H%M%S")

        json_filename = output_dir + subject_name + '_' + condition + '_' + timestamp + ".json"
        xls_filename = output_dir + subject_name + '_' + condition + '_' + timestamp + ".xlsx"

        # Save the file in JSON format
        with open(json_filename, 'w') as f:
            json.dump(self.all_data, f)

        # Save the file in Excel format
        self.write_to_excel(xls_filename)

    def write_to_excel(self, filename):
        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet()
        column = 0
        for key in self.all_data.keys():
            worksheet.write(0, column, key)
            worksheet.write_column(1, column, self.all_data[key])
            column += 1

        workbook.close()

    def load(self, filename):
        # Read data from file:
        with open(filename) as f:
            self.all_data = json.load(f)

    # Delete all data
    def clear(self):
        all_metrics = Profile().get_profile()['collected_metrics']
        for metrics in all_metrics:
            self.all_data[metrics] = []
        self.all_data['t'] = []
