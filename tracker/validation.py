def input_yes_no(prompt):
    while True:
        response = input(prompt).lower().strip()
        if response in ['yes', 'y', 'no', 'n']:
            return response in ['yes', 'y']
        print("Please enter 'yes' or 'no'.")

def input_positive_int(prompt):
    while True:
        try:
            response = input(prompt).strip()
            value = int(response)
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

            