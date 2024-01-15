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
