list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

output = [i for row in list_of_lists for num in row for i in num]
print(output)