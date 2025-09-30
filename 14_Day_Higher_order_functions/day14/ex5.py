countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def six(country):
    if len(country) == 6:
        return True
    return False

print(list(filter(six, countries)))