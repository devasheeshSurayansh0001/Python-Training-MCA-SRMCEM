'''
Reverse Words in a Sentence
 Without using Python’s built-in split() and reverse() in one line, reverse the order of words in a sentence using loops.
Input: "Python is fun"
Output: "fun is Python"
'''
def reverse_words(sentence):
    words = []
    word = ""
    
    for char in sentence + " ":  # Adding space at end to capture last word
        if char != " ":
            word += char
        else:
            if word:
                words.append(word)
                word = ""
    
    # Reverse order manually
    reversed_sentence = ""
    for i in range(len(words)-1, -1, -1):
        reversed_sentence += words[i]
        if i != 0:
            reversed_sentence += " "
    
    return reversed_sentence

# Example usage
print()
text = input("Enter a Sentence : ")
print("Reversed : ",reverse_words(text)) 

