from flask import json


def createExp(char_dictionary):
    file_content = open('static/json/explanations.json')

    # Returns JSON object as a dictionary
    expJson = json.load(file_content)
    
    exp = ["Initial state is S0"]

    if 'start' in char_dictionary:
        exp.append(expJson['start'].replace('$char$', "'"+"', '".join(char_dictionary['start'])+"'"))
    if 'end' in char_dictionary:
        exp.append(expJson['end']['step1'].replace('$char$', "'"+"', '".join(char_dictionary['end'])+"'"))
        exp.append(expJson['end']['step2'].replace('$char$', "'"+"', '".join(char_dictionary['end'])+"'"))
    
    return exp

