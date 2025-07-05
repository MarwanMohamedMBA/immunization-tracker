def input_yes_no(prompt):
    while True:
        response = input(prompt).lower().strip()
        if response in ['yes', 'y', 'no', 'n']:
            return response in ['yes', 'y']
        print("Please enter 'yes' or 'no'.")

def input_positive_int(prompt):
    while True:
        response = input(prompt).strip()
        if response.isdigit() and int(response) > 0:
            return int(response)
        print("Please enter a positive number.")
