import json

def save_patients(filename, patients_list):
    with open(filename, 'w') as file:
        json.dump(patients_list, file, indent=4)

def load_patients(filename):
    try:
        with open(filename, 'r') as file:
            patients = json.load(file)
            print("\n=== Vaccination Summary ===")
            for p in patients:
                print(p)
    except FileNotFoundError:
        print(f'Error: The file {filename} does not exist. Please save patient data first.')
    except json.JSONDecodeError:
        print(f'Error: could not parse the file {filename}. check if the filename is valid and in json format.')
    finally:
        print("Attempted to load patients from file.")
        