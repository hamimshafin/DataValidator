from datetime import datetime
import re
import csv


class DataValidator:
    def __init__(self, data):
        self.data = data


txt = "The Rain in spain"


def validate_id(id1):
    regex = r'^[0-9]+$'
    if re.match(regex, id1):
        return ""
    else:
        return "I"


def validate_name(name):
    names = name.split(',')
    if len(names) == 2:
        return ""
    else:
        return "N"


def process_name(name):
    return name.split(',')


def validate_email(email):
    regex = r'^[\w\.-]+@[\w\.-]+\.(?:edu)$'

    if re.match(regex, email):
        return ""
    else:
        return "E"


def validate_number(num):
    regex = r'^\d{3}-\d{3}-\d{4}$'

    if re.match(regex, num):
        return ""
    else:
        return "I"


def validate_date(date):
    regex = r'^\d{2}/\d{2}/\d{4}$'

    if re.match(regex, date):
        return ""
    else:
        return "D"


def validate_time(time_str):
    regex = r'^([01]?[0-9]|2[0-3]):[0-5][0-9]$'
    if re.match(regex, time_str):
        return ""
    else:
        return "T"


def swap_name(name):
    # Split the name into first name and last name
    names = name.split(',')
    if len(names) == 2:
        first_name, last_name = names
        # Swap the first name and last name
        return f"{last_name.strip()} {first_name.strip()}"
    else:
        return name


def convert_date(date):
    try:
        # Parse the input date string
        date_obj = datetime.strptime(date, '%m/%d/%Y')
        # Convert to the desired format
        return date_obj.strftime('%m-%d-%Y')
    except ValueError:
        # Handle invalid date strings (if any)
        return "Invalid Date"


def process_file():
    try:
        with open('input.csv', 'r', newline='') as input_file,\
                open('valid_file.csv', 'w', newline='') as valid_file,\
                open('invalid_file.csv', 'w', newline='') as invalid_file:

            input_reader = csv.reader(input_file, delimiter='|')
            valid_writer = csv.writer(valid_file, delimiter=',')
            invalid_writer = csv.writer(invalid_file, delimiter='|')

            for line in input_reader:
                print(line)
                error_string = ""
                data_count = len(line)

                if data_count != 6:
                    line.insert(0, 'C')
                    invalid_writer.writerow(line)
                    continue

                error_string += validate_id(line[0])
                print("Result =", error_string)

                error_string += validate_name(line[1])
                print("Result =", error_string)

                error_string += validate_email(line[2])
                print("Result =", error_string)

                error_string += validate_number(line[3])
                print("Result =", error_string)

                error_string += validate_date(line[4])
                print("Result =", error_string)

                error_string += validate_time(line[5])
                print("Result =", error_string)

                if not error_string:
                    line[1] = swap_name(line[1])
                    line[4] = convert_date(line[4])
                    valid_writer.writerow(line)
                else:
                    line.insert(0, error_string)
                    invalid_writer.writerow(line)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    process_file()
