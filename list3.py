# List1  = [1, 2, 3, 4, 5, 6, 7, 8]
# Set1  = {5, 6, 7, 8, 9, 10}
# Tasks:
# 1. Remove duplicates from my_list using a set and print the result.
# Solution:-
# list1=[1,2,3,4,5,6,7,8]
# result_set=set(list1)
# print(result_set)

# 2. Combine my_list and my_set into one collection (without duplicates), preserving the order of the list elements. Print the combined collection.
# Solution:-
# list1=[1,2,3,4,5,6,7,8]
# set1={5,6,7,8,9,10}
# print(set1.union(list1))

# 3. Find the intersection between my_list and my_set. Print the result.
# Solution:-
# list1=[1,2,3,4,5,6,7,8]
# set1={5,6,7,8,9,10}
# print(set1.intersection(list1))

# 4. Find the union of my_list and my_set. Print the result.
# Solution:-
# list1=[1,2,3,4,5,6,7,8]
# set1={5,6,7,8,9,10}
# print(set1.union(list1))

# 5. Remove the last element from my_list using the pop() method and print the modified list.
# Solution:-
# list1=[1,2,3,4,5,6,7,8]
# print(list1.pop())
# print(list1)

# 6. Remove and return an arbitrary element from my_set using the pop() method, and print the updated set.
# Solution:-

# 7. Check if all elements of my_list are present in my_set using the issubset() method. Print the result.
# Solution:
# list1=[1,2,3,4,5,6,7,8]
# set1={5,6,7,8,9,10}
# print(set1.issubset(list1))

# 8. Add elements from my_list to my_set, but only the unique elements (no duplicates) using the update() method. Print the updated set.
# Solution:-
# list1=[1,2,3,4,5,6,7,8]
# set1={5,6,7,8,9,10}
#  print(set1.update(list1))
# print(set1)

# 9. Remove the element at index 2 from my_list using the pop() method and print the modified list.
# Solution:-
# list1=[1,2,3,4,5,6,7,8]
# print(list1.pop(2))
# print(list1)

# 10. Check the difference between my_set and my_list, i.e., elements in the set but not in the list, using the difference() method. Print the result.
# Solution:-
# list1=[1,2,3,4,5,6,7,8]
# set1={5,6,7,8,9,10}
# print(set1.difference(list1))

# 11. Reverse the my_list using the reverse() method and print the result.
# Solution:-
# list1=[1,2,3,4,5,6,7,8]
# print(list1.reverse())
# print(list1)

# 12. Sort the my_list in ascending order using the sort() method and print the result.
# Solution:-
# list1=[1,2,3,4,5,6,7,8]
# print(list1.sort())
# print(list1)

# 13. Clear all elements from my_set using the clear() method and print the empty set.
# SOlution:-
# set1={5,6,7,8,9,10}
# print(set1.clear())
# print(set1)

# 14. Remove an element from my_set using the remove() method (with an existing element), and print the updated set.
# Solution:-
# set1={5,6,7,8,9,10}
# print(set1.remove(10))
# print(set1.update())
# print(set1)

# 15. Create a new set with elements that are not in my_list but are in my_set using the difference() method. Print this new set.
# Solution:-
# set2={10,11,12,9,15}
# set1={5,6,7,8,9,10}
# print(set2.difference(set1))
# print(set2)

# 16. Check if my_set and my_list are disjoint, meaning they have no common elements, using the isdisjoint() method. Print the result.
# Solution:-
# list1=[1,2,3,4,5,6,7,8]
# set1={5,6,7,8,9,10}
# print(set1.isdisjoint(list1))

# 17. Count the occurrences of the number 3 in my_list using the count() method and print the result.
# Solution:-
# list1=[1,2,3,4,5,6,7,8]
# print(list1.count(3))

# 18. Append a new element 11 to my_list using the append() method, and print the updated list.
# Solution:-
# list1=[1,2,3,4,5,6,7,8]
# print(list1.append(11))
# print(list1)

# 19. Insert the number 0 at the first position in my_list using the insert() method, and print the updated list.
# Solution:-
# list1=[1,2,3,4,5,6,7,8]
# print(list1.insert(0,0))
# print(list1)

# 20. Copy the set to another set using the copy() method and print both sets.
# Solution:-
# set1={5,6,7,8,9,10}
# set2=set1.copy()
# print(set2)