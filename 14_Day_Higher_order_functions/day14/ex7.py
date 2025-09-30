countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def six(country):
    if country[0] == 'E':
        return True
    return False

print(list(filter(six, countries)))