#                                 ## List Method Practical ##

# 1. Create an empty list and use append() to add five different numbers to it. Print the final list. -->
# Solution:-
# list=[]
# list.append(10)
# list.append(2)
# list.append(34)
# list.append(44)
# list.append(4)
# print(list)

# 2. Create a list of student name  and append a new Student name  and print the length of list .
# Solution:-
# list1=["rohan","suhani","sejal","jay"]
# list1.append("pranali")
# print(list1)
# print(len(list1))

# 3. Append a list [10, 20, 30] to another list and observe the result.
# Solution:-
# list=[10,20,30]
# list2=[40,50]
# result=list+list2
# print(result)


# 4. Create a list and make a copy using copy().
# Solution:-
# list3=[10,20,30]
# list4=list3
# list4=list3.copy()
# print(list4)

# 5. Create a list with at least 10 elements, use clear(), and check the length of the list afterward.
# Solution:-
# list3=[10,30,78,67,45,34,99,87,23,20]
# print(list3.clear())
# print(len(list3))

# 6. Create a nested list and clear only the inner list while keeping the outer list intact .
# Solution:-
# list5=[[6,9,4]]
# print(list5.clear())
# print(list5)

# 7. Given nums = [1, 2, 3, 4, 2, 2, 5, 2], find how many times 2 appears in the list.
# Solution:-
# nums=[1,2,3,4,2,2,5,2]
# print(nums)
# print(nums.count(2))

# 8. Create a list of words and find how many times a particular word appears.
# Solution:-
# charater=["Ritika","Siya","Ritika","Shreya","Ritika"]
# print(charater)
# print(charater.count("Ritika"))

# 9. Create two lists, list1 in integer variable  and list2 in String variable. Use extend() to add elements of list2 to list1.     
#    Print the final result.
# Solution:-
# list1=[1,2,3,4]
# list2=["Sherya","Soniya","Ruth","Mahima"]
# list1.extend(list2)
# print(list1)

# 10. Given fruits = ['apple', 'banana', 'cherry', 'banana', 'grape'], find the index of banana.
# Solution:-
# fruits=['apple','banana','cherry','banana','grape']
# print(fruits)
# print(fruits.index("banana"))

# 11. Insert the number 100 at the beginning of the list [10, 20, 30].
# Solution:-
# list=[10,20,30]
# list.insert(0,100)
# print(list)

# 12. Insert 'Python' at index 2 in a list of programming languages and print the result.
# Solution:-
# list6=["Java","C","RDBMS","CyberSecurity"]
# print(list6)
# list6.insert(2,"Python")
# print(list6)

# 13. Given numbers = [5, 10, 15, 20, 25], remove and print the last element using pop().
# Solution:-
# list8=[5,10,15,20,25]
# print(list8.pop())
# print(list8)

# 14. Remove an element at index 2 and print both the removed element and the updated list.
# Solution:-
# list7=[56,67,3,20,45]
# print(list7)
# list7.remove(3)
# print(list7)

# 15. Given colors = ['red', 'blue', 'green', 'blue', 'yellow'], remove the first occurrence of 'blue'.
# Solution:-
# colors=['red','blue','green','blue','yellow']
# colors.remove('blue')
# print(colors)

# 16. Reverse the list [1, 4, 9, 16, 25] and print the result.
# Solution:-
# list=[1,4,9,16,25]
# print(list)
# list.reverse()
# print(list)

# 17. Reverse a list of words and join them to form a sentence words = ["Hello", "world", "Python"].
# Solution:-
# list=["Hello","world","Python"]
# list.reverse()
# sentence=" ".join(list)
# print(sentence)

# 18. Sort a list of numbers [10, 5, 8, 3, 1] in ascending and then in descending order.
# Solution:-
# numbers=[10,5,8,3,2,1]
# print(numbers)
# numbers.reverse()
# print(numbers)


