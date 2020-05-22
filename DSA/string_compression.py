#String compression problem
#example: AAAABBBCCC should give A4B3C3

from collections import OrderedDict 

def string_compression(string):
    count = OrderedDict()
    for char in string:
        if char in count:
           count[char] += 1
        else: 
           count[char] = 1
    result = ""
    for k, v in count.items():
        result += "{}{}".format(k,v)
    return result

#without using ordered dict

def string_compression2(string):
    if len(string) == 0:
       return ""
    result = ""
    start_char = string[0]
    char_count = 1
    for char in string[1:]:
        if char == start_char:
           char_count += 1
        else:
           start_char = char
           char_count = 1
    result = result + start_char + str(char_count)
    
    return result

# Run length compression algorithm

def string_compression3(s):
    l = len(s)
    r = ""
    
    if l == 0:
       return ""
    i = 1
    cnt = 1

    while i < l:
       if s[i] == s[i-1]:
          cnt += 1
       else: 
         r = r + s[i-1] + str(cnt)
         cnt = 1
       i = i+1 
    r = r + s[i-1] + str(cnt)
    return r



print string_compression("AAAAABBBBCCCDDE")
print string_compression2("AAAAABBBBCCCDDE")
print string_compression2("")
print string_compression3("AAEEDDDDDRRRRRC")

