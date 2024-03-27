from nlq_to_re import regexBuilder

def construct_regex(charset, char_dictionary):
    regexOutput = regexBuilder.RegexBuilder()
    if 'start' in char_dictionary:
        case_no = 0 # This is to store the case number
        charset_modified = [] # This is to store the characters that appear in the char_dictionary
        for i in char_dictionary['start']:
            if 'atleast' in i:
                temp = i.split('_')
                regexOutput.specificNumberOf(temp[-2:]) # temp[-2] is the number of letters and temp[-1] is the letter
                regexOutput.oneOfTheCharacters(regexOutput.tempList) # This is to say that all the characters are 'OR' by default
                regexOutput.compileRegex() # Compile the regex
                charset_modified.append(temp[-1]) # Append the character that appears to the charset_modified
                case_no = 1
            elif 'atmost' in i:
                temp = i.split('_')
                regexOutput.atmost(temp[-2:])
                regexOutput.oneOfTheCharacters(regexOutput.tempList) # This is to say that all the characters are 'OR' by default
                regexOutput.compileRegex() # Compile the regex
                charset_modified.append(temp[-1])
                case_no = 2
            elif 'even' in i:
                temp = i.split('_')
                regexOutput.even(temp[-1])
                regexOutput.oneOfTheCharacters(regexOutput.tempList) # This is to say that all the characters are 'OR' by default
                regexOutput.compileRegex() # Compile the regex
                charset_modified.append(temp[-1]) 
                case_no = 3
                
            elif 'odd' in i:
                temp = i.split('_')
                regexOutput.odd(temp[-1])
                regexOutput.oneOfTheCharacters(regexOutput.tempList) # This is to say that all the characters are 'OR' by default
                regexOutput.compileRegex() # Compile the regex
                charset_modified.append(temp[-1])
                case_no = 4
            else:
                temp = i.split('_')
                regexOutput.regex += '('
                regexOutput.specificNumberOf(temp[-2:])
                regexOutput.compileRegex()
                regexOutput.regex += '|('
                regexOutput.compileRegex()
                regexOutput.clearTempList()
                charset_modified.append(temp[-1])
                case_no = 5
        

        # If case no = 1, use charset otherwise use charset - modified_charset
        if case_no == 1:
            regexOutput.anyNumberOf(charset)
            regexOutput.compileRegex() # Compile the regex
            regexOutput.clearTempList() # Clear the temp list variable

        elif case_no == 4 or case_no == 3:
            temp =  regexOutput.regex
            regexOutput.oneOfTheCharacters(list(set(charset) - set(charset_modified)))
            regexOutput.compileRegex()
            regexOutput.clearTempList()
            regexOutput.anyNumberOf(list(set(charset) - set(charset_modified)))
            regexOutput.compileRegex()
            regexOutput.clearTempList()
            regexOutput.anyNumberOf(charset)
            regexOutput.regex =  temp + "|("+regexOutput.regex 
            regexOutput.compileRegex() # Compile the regex
            regexOutput.regex += ")" #This is necessary because it help to segregate the final part of the OR operation
            regexOutput.clearTempList() # Clear the temp list variable

        elif case_no == 5:
            regexOutput.oneOfTheCharacters(list(set(charset) - set(charset_modified)))
            regexOutput.compileRegex() # Compile the regex
            regexOutput.clearTempList() # Clear the temp list variable
            regexOutput.anyNumberOf(charset)
            regexOutput.compileRegex()
            regexOutput.clearTempList()
            regexOutput.regex += "))"
        
        else:
            regexOutput.anyNumberOf(list(set(charset) - set(charset_modified)))
            regexOutput.compileRegex() # Compile the regex
            regexOutput.clearTempList() # Clear the temp list variable
        
        
        

    if 'contain' in char_dictionary:
        case_no = 0
        charset_modified = []
        for ch in char_dictionary['contain']:
            if 'atleast' in ch:
                temp = ch.split('_')
                charset_modified.append(temp[-1])
                case_no = 1
                ch_temp_var = temp[-1]
                number = temp[-2]
            elif 'atmost' in ch:
                temp = ch.split('_')
                charset_modified.append(temp[-1])
                case_no = 2
                ch_temp_var = temp[-1]
                number = temp[-2]
            elif 'even' in ch:
                temp = ch.split('_')
                charset_modified.append(temp[-1])
                case_no = 3
                ch_temp_var = temp[-1]
                # regexOutput.anyNumberOf(charset)
            elif 'odd' in ch:
                temp = ch.split('_')
                charset_modified.append(temp[-1])
                case_no = 4
                ch_temp_var = temp[-1]
            else:
                temp = ch.split('_')
                charset_modified.append(temp[-1])
                case_no = 5
                ch_temp_var = temp[-1]
                number = temp[-2]

        if case_no == 5:
            for n in range(int(number)):
                regexOutput.anyNumberOf(list(set(charset) - set(charset_modified))).exactString(ch_temp_var)
            regexOutput.anyNumberOf(list(set(charset) - set(charset_modified)))
            regexOutput.concat(regexOutput.tempList)
            regexOutput.compileRegex()
            regexOutput.clearTempList()

        elif case_no == 1:
            for n in range(int(number)):
                regexOutput.anyNumberOf(charset).exactString(ch_temp_var)
            regexOutput.anyNumberOf(charset)
            regexOutput.concat(regexOutput.tempList)
            regexOutput.compileRegex()
            regexOutput.clearTempList()

        elif case_no == 2:
            regexOutput.regex += '('
            for n in range(int(number)+1):
                for _ in range(n):
                    regexOutput.anyNumberOf(list(set(charset) - set(charset_modified))).exactString(ch_temp_var)
                regexOutput.anyNumberOf(list(set(charset) - set(charset_modified)))
                regexOutput.concat(regexOutput.tempList)
                regexOutput.compileRegex()
                regexOutput.clearTempList()
                regexOutput.regex += '|'
            regexOutput.regex = regexOutput.regex[:-1]
            regexOutput.regex += ')'
            print(regexOutput.regex)
        elif case_no == 3: # This is the case for 'EVEN'
            # Even cases will come like: ((b*c*)*.a.(b*c*)*.a.(b*c*)*)*
            # This makes sure that only even no. of 'a's are present
            regexOutput.anyNumberOf(list(set(charset) - set(charset_modified))).exactString(ch_temp_var).anyNumberOf(list(set(charset) - set(charset_modified))).exactString(ch_temp_var).anyNumberOf(list(set(charset) - set(charset_modified)))
            regexOutput.concat(regexOutput.tempList)
            regexOutput.loop(regexOutput.tempList[-1])
            regexOutput.compileRegex()
            regexOutput.clearTempList()
            # regexOutput.anyNumberOfOrdered(charset)
        elif case_no == 4: # This is the case for 'ODD'
            # Even cases will come like: (b*c*)*.a.((b*c*)*.a.(b*c*)*.a)*(b*c*)*
            # This makes sure that only odd no. of 'a's are present
            # regexOutput.anyNumberOf(list(set(charset) - set(charset_modified))).exactString(ch_temp_var).anyNumberOf(list(set(charset) - set(charset_modified))).exactString(ch_temp_var).anyNumberOf(list(set(charset) - set(charset_modified)))
            regexOutput.anyNumberOf(list(set(charset) - set(charset_modified))).exactString(ch_temp_var)
            regexOutput.concat(regexOutput.tempList)
            regexOutput.compileRegex()
            regexOutput.clearTempList()
            regexOutput.anyNumberOf(list(set(charset) - set(charset_modified))).exactString(ch_temp_var).anyNumberOf(list(set(charset) - set(charset_modified))).exactString(ch_temp_var)
            regexOutput.concat(regexOutput.tempList)
            regexOutput.loop(regexOutput.tempList[-1])
            regexOutput.compileRegex()
            regexOutput.clearTempList()
            regexOutput.anyNumberOf(list(set(charset) - set(charset_modified)))
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
                charset_modified.append(temp[-1]) # Append the character that appears to the charset_modified
                case_no = 1
                regexOutput.specificNumberOf(temp[-2:]) # temp[-2] is the number of letters and temp[-1] is the letter
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
                regexOutput.regex += '('
                regexOutput.compileRegex()

        # If case no = 1, use charset otherwise use charset - modified_charset
        if case_no == 1:
            regexOutput.anyNumberOf(charset)
            regexOutput.compileRegex() # Compile the regex
            regexOutput.clearTempListPartially(1)
            regexOutput.oneOfTheCharacters(regexOutput.tempList) # This is to say that all the characters are 'OR' by default
            regexOutput.compileRegex() # Compile the regex
            regexOutput.clearTempList() # Clear the tempList variable

        elif case_no == 3 or case_no == 4:
            regexOutput.compileRegex() # Compile the regex
            temp = regexOutput.regex
            regexOutput.regex += '|('
            
            regexOutput.anyNumberOf(charset)
            regexOutput.compileRegex()
            regexOutput.clearTempList()
            
            regexOutput.oneOfTheCharacters(list(set(charset) - set(charset_modified)))
            regexOutput.compileRegex()
            regexOutput.clearTempList()
            
            regexOutput.anyNumberOf(list(set(charset) - set(charset_modified)))
            regexOutput.compileRegex()
            regexOutput.clearTempList()
            regexOutput.regex += temp
            regexOutput.regex += ')'

        elif case_no == 5:
            regexOutput.regex += '|('
            regexOutput.anyNumberOf(charset)
            regexOutput.compileRegex()
            regexOutput.clearTempListPartially(1)
            regexOutput.oneOfTheCharacters(list(set(charset) - set(charset_modified)))
            regexOutput.loopAtleastOnce(regexOutput.tempList[-1])
            regexOutput.compileRegex()
            regexOutput.clearTempListPartially(2)
            regexOutput.oneOfTheCharacters(regexOutput.tempList) # This is to say that all the characters are 'OR' by default
            regexOutput.compileRegex()
            regexOutput.clearTempList()
            regexOutput.regex += '))'
        
        else:
            regexOutput.anyNumberOf(list(set(charset) - set(charset_modified)))
            regexOutput.compileRegex() # Compile the regex
            regexOutput.clearTempListPartially(1)  # Clear only the last 1 element of tempList. The number passed is the number of elements to be cleared from the end of the list
            regexOutput.oneOfTheCharacters(regexOutput.tempList) # This is to say that all the characters are 'OR' by default
            regexOutput.compileRegex() # Compile the regex
            regexOutput.clearTempList() # Clear the tempList variable

    return regexOutput.regex