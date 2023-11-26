from nlq_to_re import regexBuilder

def construct_regex(charset, char_dictionary):
    regexOutput = regexBuilder.RegexBuilder()

    if 'start' in char_dictionary:
        regexOutput.oneOfTheCharacters(char_dictionary['start']).anyNumberOf(charset)
    if 'contain' in char_dictionary:
        for ch in char_dictionary['contain']:
            regexOutput.exactString(ch).anyNumberOf(charset)
    if 'end' in char_dictionary:
        regexOutput.oneOfTheCharacters(char_dictionary['end'])

    return regexOutput.regex