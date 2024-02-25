from nlq_to_re import regexBuilder

def construct_regex(charset, char_dictionary):
    regexOutput = regexBuilder.RegexBuilder()
    if 'start' in char_dictionary:
        case_no = 0
        charset_modified = []
        for i in char_dictionary['start']:
            if 'atleast' in i:
                temp = i.split('_')
                regexOutput.specificNumberOf(temp[-2:])
                charset_modified.append(temp[-1])
                case_no = 1
            elif 'atmost' in i:
                temp = i.split('_')
                regexOutput.atmost(temp[-2:])
                charset_modified.append(temp[-1])
                case_no = 2
            else:
                temp = i.split('_')
                regexOutput.specificNumberOf(temp[-2:])
                charset_modified.append(temp[-1])
                case_no = 3
        regexOutput.oneOfTheCharacters(regexOutput.tempList)
        regexOutput.compileRegex()
        if case_no == 1:
            regexOutput.anyNumberOf(charset)
        else:
            regexOutput.anyNumberOf(list(set(charset) - set(charset_modified)))
        regexOutput.compileRegex()


    if 'contain' in char_dictionary:
        for ch in char_dictionary['contain']:
            if 'atleast' in ch:
                temp = ch.split('_')
                regexOutput.anyNumberOf(charset).exactString(temp[-1]).anyNumberOf(charset)
            elif 'atmost' in ch:
                temp = ch.split('_')
                regexOutput.anyNumberOf(charset).exactString(temp[-1]).anyNumberOf(charset)
            else:
                temp = ch.split('_')
                regexOutput.anyNumberOf(charset).exactString(temp[-1]).anyNumberOf(charset)
        regexOutput.concat(regexOutput.tempList)
        regexOutput.compileRegex()



    if 'end' in char_dictionary:
        case_no = 0
        charset_modified = []
        for i in char_dictionary['end']:
            if 'atleast' in i:
                temp = i.split('_')
                charset_modified.append(temp[-1])
                case_no = 1
                regexOutput.specificNumberOf(temp[-2:])
            elif 'atmost' in i:
                temp = i.split('_')
                charset_modified.append(temp[-1])
                case_no = 2
                regexOutput.atmost(temp[-2:])
            else:
                temp = i.split('_')
                charset_modified.append(temp[-1])
                case_no = 3
                regexOutput.specificNumberOf(temp[-2:])
        if case_no == 1:
            regexOutput.anyNumberOf(charset)
        else:
            regexOutput.anyNumberOf(list(set(charset) - set(charset_modified)))
        regexOutput.compileRegex()
        regexOutput.clearTempListPartially(1)
        regexOutput.oneOfTheCharacters(regexOutput.tempList)
        regexOutput.compileRegex()

    return regexOutput.regex