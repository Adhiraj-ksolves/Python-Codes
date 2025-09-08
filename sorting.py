# Searching and Sorting Problem: > Create a function that will sort the array of string based on the length of string. e.g.: ['deepak', 'aman', 'sam', 'naman', 'mohit'] =>
# ['sam', 'aman', 'naman', 'mohit', 'deepak'] > use sorted, lambda function

Names = ['deepak', 'aman', 'sam', 'naman', 'mohit']

SortedList = sorted(Names, key=lambda x : len(x),reverse=True)

print(SortedList)