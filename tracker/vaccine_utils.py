def is_eligible(age):
    return age >= 18

def can_vaccinate(has_appointment):
    return has_appointment  # just return the boolean

def valid_date(vaccine_date):
    return (len(vaccine_date) == 10 and vaccine_date[4] == '-' and vaccine_date[7] == '-' and
            vaccine_date[:4].isdigit() and vaccine_date[5:7].isdigit() and vaccine_date[8:].isdigit())
