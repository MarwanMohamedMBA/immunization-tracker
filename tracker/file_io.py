import json

def save_patients(filename, patients_list):
    with open(filename, 'w') as file:
        json.dump(patients_list, file, indent=4)

def load_patients(filename):
    with open(filename, 'r') as file:
        return json.load(file)
