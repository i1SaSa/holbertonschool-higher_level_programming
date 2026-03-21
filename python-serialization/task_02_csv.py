import csv
import json
import os


def convert_csv_to_json(csv_file, json_file=None):
    if csv_file and os.path.exists(csv_file):

        if not json_file:
            json_file = csv_file.rsplit('.', 1)[0] + '.json'

        with open(csv_file, mode='r', newline='', encoding='utf-8') as csvfile:
            data = list(csv.DictReader(csvfile))

        with open(json_file, mode='w', encoding='utf-8') as jsonfile_out:
            json.dump(data, jsonfile_out, indent=4, ensure_ascii=False)

        return True

    return False
