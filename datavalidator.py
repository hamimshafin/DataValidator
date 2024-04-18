import re


class DataValidator:
    def __init__(self, data):
        self.data = data


txt = "The Rain in spain"


def validate_id(self):
    x = re.search("^The. *Spain$", txt)
    if not re.search("[0-9]", self.data):
        raise ValueError


def validate_name(name):
    names = name.split(',')
    if len(names) == 2:
        return ""
    else:
        return "N"
