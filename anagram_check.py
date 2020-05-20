#check if the given two strings are anagrams or not
#example of an anagram "public relations" is anagram of "crap built on lies"


def anagram_check(s1, s2):

    s1=s1.replace(" ", "").lower()
    s2=s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)


def anagram_check2(s1, s2):
    
    s1=s1.replace(" ", "").lower()
    s2=s2.replace(" ", "").lower()
    
    if len(s1) != len(s2):
       return False

    count = {}
  
    for letter in s1:
        if letter in count:
           count[letter] += 1
        else:
           count[letter] = 1

    for letter in s2:
        if letter in count:
           count[letter] -= 1
        else:
           count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False
    return True


assert anagram_check("public relations", "crap built on lies")
assert anagram_check("god", "dog") 
assert anagram_check2("public relations", "crap built on lies")
assert anagram_check2("god", "dog")
assert anagram_check("naveen", "kandra") == False 
