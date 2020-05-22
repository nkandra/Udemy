#return True only if all the character in the string are unique


def unique_char(s):
    if len(set(s)) == len(s):
       return True
    return False

def unique_char2(s):
    char_set = set()
    for char in s:
      if char in char_set:
         return False
      else: 
         char_set.add(char)

    return True

assert unique_char("asfght") == True
assert unique_char("asfghta") == False
assert unique_char2("asfght") == True
assert unique_char2("asfghta") == False
 
