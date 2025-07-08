from tracker.validation import input_yes_no, input_positive_int
from tracker.vaccine_utils import is_eligible, can_vaccinate, valid_date, validate_date_or_raise
from tracker.file_io import save_patients, load_patients
from tracker.api_utils import get_vaccine_data


def main():
    total_patients = input_positive_int("Enter the number of patients: ")
    ineligible_patients = 0
    eligible_patients = 0
    total_vaccines = 0
    patients_list = []  

    for i in range(total_patients):
        print(f"\n--- Patient {i + 1} ---\n")
        name = input("Enter the patient's name: ").strip()
        age = input_positive_int("Enter the patient's age: ")
        if not is_eligible(age):
            print(f"{name} is not eligible for vaccination due to age.")
            ineligible_patients += 1
            continue
        eligible_patients += 1
        has_appointment = input_yes_no("Does the patient have an appointment? (yes/no): ")
        if not can_vaccinate(has_appointment):
            print(f"{name} cannot be vaccinated without an appointment.")
            continue
        
        while True:
            try:
                vaccine_date = input("Enter the vaccine date (YYYY-MM-DD): ").strip()
                validate_date_or_raise(vaccine_date)
                break

            except ValueError as e:
                print(e)
                
        
        vaccine_type = input("Enter the vaccine type: ").strip()
        total_vaccines += 1
        patient = {
            "name": name,
            "age": age,
            "has_appointment": has_appointment,
            "vaccine_date": vaccine_date,
            "vaccine_type": vaccine_type,
        }
        patients_list.append(patient)

    save_patients("patients.json", patients_list)
    if input_yes_no("Would you like to see the vaccination summary? (yes/no): ") :
        load_patients("patients.json")

        print("\n=== Vaccination Summary ===")

    for patient in patients_list:
        print(f"Name: {patient['name']}")
        print(f"Age: {patient['age']}")                  
        print(f"Appointment: {'Yes' if patient['has_appointment'] else 'No'} ")
        print(f"Vaccine Date: {patient['vaccine_date']}")
        print(f"Vaccine Type: {patient['vaccine_type']}")
    print(f"Total patients: {total_patients}")
    print(f"Eligible patients: {eligible_patients}")
    print(f"Ineligible patients: {ineligible_patients}")
    print(f"Total vaccines administered: {total_vaccines}")
    print("Patient data saved to patients.json")
    # ✅ NEW: Pull real-time API data
    print("\n=== CDC COVID Vaccination Data Snapshot ===")
    api_data = get_vaccine_data()

    if api_data is not None:
        for entry in api_data[:3]:  # show only first 3 for now
            print(f"Date: {entry.get('date')}")
            print(f"Location: {entry.get('location')}")
            print(f"Doses Administered: {entry.get('administered')}")
            print(f"Fully Vaccinated: {entry.get('series_complete_yes')}")
            print("-" * 40)
    else:
        print("Could not fetch CDC vaccination data.")

    print("Thank you for using the vaccination tracker!")
    

if __name__ == "__main__":
    main()
