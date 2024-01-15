#Example 1
#input: 4a output: aaaa
#input: a2b10c output: abbcccccccccc

def decode_string(s: str) -> str:
  solution_str = ""

  # using a string to make our lives easier
  count = ""

  for char in s:
    if char.isDigit():
      count += char
    else:
      if count == "":
        solution_str += char
      else:
        # multiplying a string by an int creates copies of the string!
        solution_str += int(count) * char
        count = ""

  return solution_str

#input: ab2[c]3[de4[f]] output: abccdeffffdeffffdeffff
def decode_string(s: str) -> str:
  return_string = ""
  count = ""
  contents = ""
  group = 0

  for char in s:
    if group == 0:
      if char.isdigit():
        count += char
      elif char == "[":
        group += 1
      else:
        return_string += char
    else:
      if char == "]":
        group -= 1

        if group == 0:
          # we found the end of a grouping
          # expand it and add it to our output string.
          return_string += int(count) * self.decode_string(contents)
          count = ""
           contents = ""
        else:
          contents += char
      else:
        if char == "[":
          group += 1

        contents += char

  return return_string

#Using stack
class Encoding:
    def __init__(self, count:str = "", contents:str = "") -> None:            
        self.count = count
        self.contents = contents

def decode_string(s: str) -> str:
    encoding_stack = [Encoding()]
    count = ""
        
    for char in s:
        if char.isdigit():
            count += char
        elif char == "[":
            encoding_stack.append(Encoding(count=count, contents=""))
            count = ""
        elif char == "]":
            encoding = encoding_stack.pop()
            expanded_encoding = int(encoding.count) * encoding.contents
            encoding_stack[-1].contents += expanded_encoding
        else:
            encoding_stack[-1].contents += char
        
    return encoding_stack[0].contents
