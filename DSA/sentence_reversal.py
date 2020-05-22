# Reverse the sentence without any trailing spaces
#"this is the best" should be "best the is this"


# Using python shortcut
def sentence_reversal(string):
    string = string.strip()
    return " ".join(string.split(" ")[::-1])

# Not using split
def sentence_reversal2(string):
    string = string.strip()
    stack = []
    word_start_index = 0
    for i in range(len(string)):
       if string[i] == " ":
          stack.append(string[word_start_index:i])
          word_start_index = i+1
    stack.append(string[word_start_index:])
    result = ""    
    for i in range(len(stack)-1):
        result += stack.pop()
        result += " "
    result += stack[-1]
    return result
print sentence_reversal("   this is the best  ") 
print sentence_reversal2("   this is the best  ") 
