inp = input()
esc = 0
if "\\" in inp:
    inp = inp.replace("\\", "")
    esc = 1
regex = list(inp[:inp.find("|")])
string = list(inp[inp.find("|") + 1:])

def regex_function(regex, string):
    if len(regex) == 0:
        return True
    if len(string) == 0 and regex == ['$']:
        return True
    if len(string) == 0:
        return False

    if esc:
        if regex[0] == string[0] :
            return regex_function(regex[1:], string[1:])
        else:
            return False
    else:
        
        
        if '?' in regex:
            if regex[1] == '?':
                ''' Condition about the first character of string matching the character before ? of the regex. 2nd case'''
                if regex[0] in ['.', string[0]]:
                    return regex_function(regex[2:], string[1:])
                ''' If not, then it is skipped and we pass the rest of the regex and the unmodified string. 1st case'''
                return regex_function(regex[2:], string)
        
        if '*' in regex:
            if regex[1] == '*':
                ''' The preceding character occurs once or more. 2nd case'''
                if (regex[0] in ['.', string[0]]) and len(string) > 1:
                    return regex_function(regex, string[1:])
                ''' The preceding character occurs zero time. 1st case.'''
                return regex_function(regex[2:], string)
        
        if '+' in regex:
            if regex[1] == '+':
                ''' Checking the preceding character. If it occurs we pass the function that slides or not the string
                depending of its size and if it matches the regex.'''
                if regex[0] in ['.', string[0]]:
                    return slice_string(regex[2:], string[1:])
                ''' If the preceding character doesnt occur we return a False.'''
                return False

    if regex[0] == string[0] or regex[0] == ".":
        return regex_function(regex[1:], string[1:])
    else:
        return False
            
def slice_string(regex, string):
    if len(regex) > 0 and regex[0] == '^':
        return regex_function(regex[1:], string)
    if regex == ['$'] and len(string) > 0:
        return False    
    if regex_function(regex, string):
        return True
    elif len(string) == 0:        
        return False
    else:
        return slice_string(regex, string[1:])    

print(slice_string(regex, string))
