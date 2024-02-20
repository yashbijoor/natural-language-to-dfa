from nlq_to_re import regexBuilder

def construct_regex(charset, char_dictionary):
    regexOutput = regexBuilder.RegexBuilder()
    if 'start' in char_dictionary: 
        for i in char_dictionary['start']:
            if '_' in i:
                temp = i.split('_')
                regexOutput.specificNumberOf(temp)
            else:
                regexOutput.exactString(i)
        regexOutput.oneOfTheCharacters(regexOutput.tempList)
        regexOutput.compileRegex()
        regexOutput.anyNumberOf(charset)
        regexOutput.compileRegex()


    if 'contain' in char_dictionary:
        for ch in char_dictionary['contain']:
            if '_' in ch:
                temp = ch.split('_')
                regexOutput.anyNumberOf(charset).exactString(temp[-1]).anyNumberOf(charset)
        regexOutput.concat(regexOutput.tempList)
        regexOutput.compileRegex()



    if 'end' in char_dictionary:
        regexOutput.anyNumberOf(charset)
        regexOutput.compileRegex()
        for i in char_dictionary['end']:
            if '_' in i:
                temp = i.split('_')
                regexOutput.specificNumberOf(temp)
            else:
                regexOutput.exactString(i)
        regexOutput.oneOfTheCharacters(regexOutput.tempList)
        regexOutput.compileRegex()

    return regexOutput.regex