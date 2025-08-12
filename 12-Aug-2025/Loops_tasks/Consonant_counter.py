'''
Count Consonants in a String
 Write a program to count how many consonants are in a given string.
Input: "hello world"
Output: 7
'''
def count_consonants(s):
    vowels = "aeiouAEIOU"
    count = 0
    for i in s:
        if i.isalpha() and i not in vowels:  # Only letters & not vowels
            count += 1
    return count

# Example usage
text = input("Enter a Sentence : ")
print("Number of consonants:", count_consonants(text))

