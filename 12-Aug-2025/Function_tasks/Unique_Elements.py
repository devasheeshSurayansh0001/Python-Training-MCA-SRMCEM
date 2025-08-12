'''
Unique Elements Function
 Write a function unique_elements(lst) that returns a list containing only the unique elements from the given list (order should be preserved).
Input: [1, 2, 2, 3, 4, 1, 5]
Output: [1, 2, 3, 4, 5]
'''
def unique_elements(lst):
  uniq_list=[]
  for i in lst:
    if i not in uniq_list:
      uniq_list.append(i)
  return uniq_list
print("Unique Elements Function")
print("Inputs : [1, 2, 2, 3, 4, 1, 5]")
print("Output :",unique_elements([1, 2, 2, 3, 4, 1, 5]))

