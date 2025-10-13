import re


def validate_phone(phone):
    pattern = r'^(\(\d{3}\)\s|\d{3}-)\d{3}-\d{4}$'
    return re.fullmatch(pattern, phone) is not None


def validate_ssn(ssn):
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return re.fullmatch(pattern, ssn) is not None


def validate_zip(zip):
    pattern = r'^\d{5}(-\d{4})?$'
    return re.fullmatch(pattern, zip) is not None


def main():
    print("Check Info Here\n")

    phone = input("Enter your phone number in either of the following formats (012) 345-6789 or 012-345-6789:\n ")
    ssn = input ("Enter your SSN (ex. 123-45-6789) :\n ")
    zip = input("Enter your zip (ex. 12345 or 12345-6789):\n ")

    print("Results:\n")

    if validate_phone(phone):
        print("Phone number is valid")
    else:
        print("Phone number is invalid")
    if validate_ssn(ssn):
        print("SSN is valid")
    else:
        print("SSN is invalid")
    if validate_zip(zip):
        print("Zip is valid")
    else:
        print("Zip is invalid")

if __name__ == '__main__':
    main()
