'''
Character Frequency Counter
 Write a function char_frequency(s) that returns a dictionary with characters as keys and their frequency as values.
Input: "hello"
Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
'''
def char_frequency(s):
  freq_dic = {}
  for i in s:
    if i in freq_dic:
      freq_dic[i]+=1
    else:
      freq_dic[i] = 1
  return freq_dic
print()
print("Character Frequency Counter Function")
text=input("Enter a text : ")
print(char_frequency(text))