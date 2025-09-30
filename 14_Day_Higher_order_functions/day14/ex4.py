countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def landless(country):
    if "land" in country:
        return False
    return True

print(list(filter(landless, countries)))