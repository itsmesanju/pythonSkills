def rev_sentence(sentence): 
  
    # first split the string into words 
    words = sentence.split(' ') 
  
    # then reverse the split string list and join using space 
    reverse_sentence = ' '.join(reversed(words)) 
  
    # finally return the joined string 
    return reverse_sentence 
  
if __name__ == "__main__": 
    input = 'geeks quiz practice code'
    print (rev_sentence(input))



### ALTERNATIVE

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        filtered_words = [s for s in words if s != '']
        return ' '.join(filtered_words[::-1])
