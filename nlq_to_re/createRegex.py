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
            elif 'even' in i:
                temp = i.split('_')
                regexOutput.even(temp[-1])
                charset_modified.append(temp[-1])
                case_no = 3
            elif 'odd' in i:
                temp = i.split('_')
                regexOutput.odd(temp[-1])
                charset_modified.append(temp[-1])
                case_no = 4
            else:
                temp = i.split('_')
                regexOutput.specificNumberOf(temp[-2:])
                charset_modified.append(temp[-1])
                case_no = 5
        regexOutput.oneOfTheCharacters(regexOutput.tempList)
        regexOutput.compileRegex()
        if case_no == 1:
            regexOutput.anyNumberOf(charset)
        else:
            regexOutput.anyNumberOf(list(set(charset) - set(charset_modified)))
        regexOutput.compileRegex()
        regexOutput.clearTempList()


    if 'contain' in char_dictionary:
        case_no = 0
        charset_modified = []
        for ch in char_dictionary['contain']:
            if 'atleast' in ch:
                temp = ch.split('_')
                charset_modified.append(temp[-1])
                case_no = 1
                regexOutput.anyNumberOf(charset).exactString(temp[-1]).anyNumberOf(charset)
            elif 'atmost' in ch:
                temp = ch.split('_')
                charset_modified.append(temp[-1])
                case_no = 2
                regexOutput.anyNumberOf(charset).exactString(temp[-1]).anyNumberOf(charset)
            elif 'even' in ch:
                temp = ch.split('_')
                charset_modified.append(temp[-1])
                case_no = 3
                ch_even_odd = temp[-1]
            elif 'odd' in ch:
                temp = ch.split('_')
                charset_modified.append(temp[-1])
                case_no = 4
                ch_even_odd = temp[-1]
            else:
                temp = ch.split('_')
                charset_modified.append(temp[-1])
                case_no = 5
                regexOutput.anyNumberOf(charset).exactString(temp[-1]).anyNumberOf(charset)
        # if case_no == 1:
        #     regexOutput.anyNumberOf(charset)
        # elif case_no == 3:
        #     regexOutput.exactString
        # else:
        #     regexOutput.anyNumberOf(list(set(charset) - set(charset_modified)))
        if case_no == 3:
            regexOutput.anyNumberOf(list(set(charset) - set(charset_modified))).exactString(ch_even_odd).anyNumberOf(list(set(charset) - set(charset_modified))).exactString(ch_even_odd).anyNumberOf(list(set(charset) - set(charset_modified)))
            regexOutput.concat(regexOutput.tempList)
            regexOutput.loop(regexOutput.tempList[-1])
            regexOutput.compileRegex()
            regexOutput.clearTempList()
        elif case_no == 4:
            regexOutput.anyNumberOf(list(set(charset) - set(charset_modified))).exactString(ch_even_odd).anyNumberOf(list(set(charset) - set(charset_modified))).exactString(ch_even_odd).anyNumberOf(list(set(charset) - set(charset_modified)))
            regexOutput.concat(regexOutput.tempList)
            regexOutput.loop(regexOutput.tempList[-1])
            regexOutput.exactString(ch_even_odd)
            regexOutput.concat(regexOutput.tempList[-2:])
            regexOutput.compileRegex()
            regexOutput.clearTempList()
        else:
            regexOutput.concat(regexOutput.tempList)
            regexOutput.compileRegex()
            regexOutput.clearTempList()


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
            elif 'even' in i:
                temp = i.split('_')
                regexOutput.even(temp[-1])
                charset_modified.append(temp[-1])
                case_no = 3
            elif 'odd' in i:
                temp = i.split('_')
                regexOutput.odd(temp[-1])
                charset_modified.append(temp[-1])
                case_no = 4
            else:
                temp = i.split('_')
                charset_modified.append(temp[-1])
                case_no = 5
                regexOutput.specificNumberOf(temp[-2:])
        if case_no == 1:
            regexOutput.anyNumberOf(charset)
        else:
            regexOutput.anyNumberOf(list(set(charset) - set(charset_modified)))
        regexOutput.compileRegex()
        regexOutput.clearTempListPartially(1)
        regexOutput.oneOfTheCharacters(regexOutput.tempList)
        regexOutput.compileRegex()
        regexOutput.clearTempList()

    return regexOutput.regex