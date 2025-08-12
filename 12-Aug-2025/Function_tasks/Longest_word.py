'''
Find Longest Word
 Write a function longest_word(sentence) that returns the longest word from a given sentence.
Input: "Python is an amazing programming language"
Output: "programming"
'''
def longest_word(sentence):
  words = sentence.split()  # Split the sentence into a list of words
  longest = max(words, key=len)  # Find the word with the maximum length
  return longest
print()
print("Longest Word Function")
print("Input : Python is a programming language")
print("Output :",longest_word("Python is a programming language"))

