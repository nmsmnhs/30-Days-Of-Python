countries = [2, 'Finland', 'Sweden', 60, 'Norway', ['Iceland']]

def get_string_lists(item):
    if isinstance(item, str) == True:
        return True
    return False

print(list(filter(get_string_lists, countries)))