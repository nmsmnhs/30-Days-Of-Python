import functools
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_even_sum = functools.reduce(lambda x,y: x+y, filter(lambda x : x%2 == 0, list(map(lambda x: x**2, numbers))))
                    
                    
print(squared_even_sum)