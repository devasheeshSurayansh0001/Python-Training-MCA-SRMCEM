'''
List Rotation
 Write a function rotate_list(lst, k) that rotates the elements of a list to the right by k positions.
Input: ([1, 2, 3, 4, 5], 2)
Output: [4, 5, 1, 2, 3]
'''
def rotate_list(lst,k):
  if k>=len(lst):
    return "value of k for requested rotation is larger than index of list"
  return lst[-k:]+lst[:-k]
print()
print("List Rotation")
print(rotate_list([1, 2, 3, 4, 5], 2))

