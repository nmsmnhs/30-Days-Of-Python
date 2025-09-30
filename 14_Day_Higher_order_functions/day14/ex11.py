import functools
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def concat(x, y):
    if countries.index(y) == len(countries)-1:
        return x + ", and " + y
    return x + ", " + y

print(functools.reduce(concat, countries), "are north European countries")