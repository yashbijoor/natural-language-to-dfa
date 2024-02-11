from flask import json


def createExp(char_dictionary, charset):
    file_content = open('static/json/explanations.json')

    # Returns JSON object as a dictionary
    expJson = json.load(file_content)
    
    exp = ["Initial state is S0"]

    if 'start' in char_dictionary:
        exp.append(expJson['start']['step1'].replace('$char$', "'"+"'or '".join(char_dictionary['start'])+"'"))
        # To check if there is and ending or containing condition in the query
        if ('end' not in char_dictionary ) and ('contain' not in char_dictionary):
            exp.append(expJson['start']['step2'].replace('$char$', "'"+"', '".join(charset)+"'"))
    if 'contain' in char_dictionary:
        exp.append(expJson['contain']['step1'].replace('$char$', "'"+"'or '".join(char_dictionary['contain'])+"'"))
        # To check if there is a ending condition in the query
        if ('end' not in char_dictionary ):
            exp.append(expJson['contain']['step2'].replace('$char$', "'"+"', '".join(charset)+"'"))
    if 'end' in char_dictionary:
        exp.append(expJson['end']['step1'].replace('$char$', "'"+"'or '".join(char_dictionary['end'])+"'"))
        exp.append(expJson['end']['step2'].replace('$char$', "'"+"'or '".join(char_dictionary['end'])+"'"))
    
    return exp

