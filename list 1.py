list2 = [10, 20, 30, [40, 50, [60, 80, 90], 100, 110, 120], [112, 114, 116], 221, 226, 336]

# 1. Access First-Level Elements
# Solution:-
# print(list2[0])

# 2. What is the output of list2[0] and list2[3]?
# Solution:-
# print(list2[0])   Output ;- 10
# print(list2[3])   Output:- [40, 50, [60, 80, 90], 100, 110, 120]

# 3. Extract the list [40, 50, [60, 80, 90], 100, 110, 120] using indexing.
# Solution:-
# print(list2[3])

# 4. Retrieve 60, 80, and 90 from the nested list using indexing.
# Solution:-
# print(list2[3][2])

# 5. What is the output of list2[4][1]?
# Solution:-
# print(list2[4][1])

# 6. Write a statement to access the element 336.
# Solution:-
# print(list2[7])
 		
# 8. The second-to-last sub-list ([112, 114, 116]).
# Solution:-
# print(list2[4])

# 9. Access 110 from the sub-list [40, 50, [60, 80, 90], 100, 110, 120].
# Solution:-
# print(list2[3])

# 10. Retrieve the element 116 from the list [112, 114, 116].
# Solution:-
# print(list2[4])
			
#11. Extract 40 from [40, 50, [60, 80, 90], 100, 110, 120].
# Solution:-
# print(list2[3])

# 12. Write a slice to extract [30, [40, 50, [60, 80, 90], 100, 110, 120]].
# Solution:-
# print(list2[2:4])

# 13. Extract [100, 110, 120] from the nested sub-list [40, 50, [60, 80, 90], 100, 110, 120].
# Solution:-
# print(list2[3][3:6]) 

# 14. Write a slice to reverse the entire list2.
# Solution:-
# list2.reverse()
# print(list2)

# 15. Reverse the list [112, 114, 116].
# Solution:-
# list2[4].reverse()
# print(list2[4])

# 16. Write a slice to get [60, 80, 90].
# Solution:-
# print(list2[3][2])

# 17. From the main list, extract [10, 30, [112, 114, 116]] using slicing.
# Solution:-
# print([list2[0],list2[2],list2[4]])

# 18. Slice to extract [221, 226, 336] from the main list.
# Solution:-
# print(list2[5:8])

# 19. Write a slice to extract [40, 50, [60, 80, 90]].
# Solution:-
# print(list2[3][:3])

# 20. Write a slice to get [10, 30, [112, 114, 116], 226].
# Solution:-
# print([list2[0],list2[2],list2[4]],list2[6])

# 21. How many elements are in list2[3] and list2[4]?
# Solution:-
# print(list2.count[3])
# print(list2[4])

# 22. Write the statement to extract [112, 114, 116] from list2.
# Solution:-
# print(list2[4])

# 23. Retrieve the element 80 from the third-level nested list [60, 80, 90].
# Solution:-
# print(list2[3][2][1])

# 24. Access 110 using negative indexing.
# Solution:-
# print(list2[3][-2])

# 25. Extract the element 100 using a combination of indexes.
# Solution:-
# print(list2[3][3])

# 26. Retrieve 90 from the list [60, 80, 90].
# Solution:-
# print(list2[3][2][2])

# 27. Using negative indexing, extract 226 from list2.
# Solution:-
# print(list2[-2])

# 28. What happens when you try list2[3][5][0]? Explain why.
# Solution:-
# print(list2[3][5][0])  TypeError: 'int' object is not subscriptable

# 29. Retrieve the middle element 50 from [40, 50, [60, 80, 90], 100, 110, 120].
# Solution:-
# print(list2[3][1])

# 30. Write statements to extract the first element (10) and the last element (336) of list2.
# Solution:-
# print((list2[0]),(list2[7]))

# 31. Retrieve 20 from list2 using both positive and negative indexing.
# Solution:-
# print(list2[1])
# print(list2[-7])

# 32. Write a slice to extract the first 4 elements of list2.
# Solution:-
# print(list2[0:5])

# 33. Slice to extract [30, [40, 50, [60, 80, 90], 100, 110, 120], [112, 114, 116]].
# Solution:-
# print(list2[2:5])

# 34. Slice the main list to extract every second element.
# Solution:-
# print(list2[::2])

# 35. Write a slice to reverse all elements in list2.
# Solution:-
# print(list2[::-1])

# 36. Reverse [40, 50, [60, 80, 90], 100, 110, 120].
# Solution:-
# print(list2[3][::-1])

# 37. Slice to get the last two sub-lists: [[112, 114, 116], 221, 226, 336].
# Solution:-
# print(list2[4:8])

# 38. Write a slice to extract [60, 80] from the list [60, 80, 90].
# Solution:-
# print(list2[3][2][0:2])

# 39. Slice to extract [50, [60, 80, 90], 100] from [40, 50, [60, 80, 90], 100, 110, 120].
# Solution:-
# print(list2[3][1:4])

# 40. How many elements are in list2[3][2]?
# Solution:-
# print(list2[3][2]) There are three elements in list

# 41. Extract every second element from [40, 50, [60, 80, 90], 100, 110, 120] using slicing with a step.
# Solution:-
# print(list2[3][0:5:2])

# 42. Extract [80, 90] by combining indexing and slicing from [60, 80, 90].
# Solution:-
# print(list2[3][2][1:3])

# 43.Write a slice to reverse [60, 80, 90] using negative steps.
# Solution:-
# print(list2[3][2][2::-1]

# 44. Combine slicing and indexing to extract [50, 100, 120] from [40, 50, [60, 80, 90], 100, 110, 120].
# Solution:-
# print(list[3][1::2])

# 45. Retrieve 50 and 80 in a single operation using slicing and indexing.
# Solution:-
# print(list2[3][1:3])

# 46. Reverse both [40, 50, [60, 80, 90], 100, 110, 120] and [112, 114, 116] in a single operation.
# Solution:-
# print(list2[3][1::-1][4::-1]



