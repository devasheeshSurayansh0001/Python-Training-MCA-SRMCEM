'''
Sum of Digits Function
 Write a function sum_of_digits(num) that calculates and returns the sum of digits of a number.
Input: 12345
Output: 15
'''
def sum_of_digits(num):
  sum=0
  while num>0:
    sum = sum + num%10
    num=num//10
  return sum
print()
print("Sum Of Digits Function")
n=int(input("Enter a number : "))
print("Sum of digits of ",n,":",sum_of_digits(n))

