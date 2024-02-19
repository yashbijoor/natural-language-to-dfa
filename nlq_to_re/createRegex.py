from nlq_to_re import regexBuilder

def construct_regex(charset, char_dictionary):
    # print(char_dictionary)
    regexOutput = regexBuilder.RegexBuilder()
    if 'start' in char_dictionary: 
        for i in char_dictionary['start']:
            if '_' in i:
                temp = i.split('_')
                regexOutput.specificNumberOf(temp)
            else:
                regexOutput.oneOfTheCharacters(char_dictionary['start'])
        regexOutput.anyNumberOf(charset)
        # print(regexOutput)


    if 'contain' in char_dictionary:
        for ch in char_dictionary['contain']:
            regexOutput.anyNumberOf(charset).exactString(ch).anyNumberOf(charset)


    if 'end' in char_dictionary:
        # print(char_dictionary)
        for i in char_dictionary['end']:
            if '_' in i:
                temp = i.split('_')
                regexOutput.anyNumberOf(charset).specificNumberOf(temp)
                
            else:
                regexOutput.anyNumberOf(charset).oneOfTheCharacters(char_dictionary['start'])
        print(regexOutput)

    return regexOutput.regex