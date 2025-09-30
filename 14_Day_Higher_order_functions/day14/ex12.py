from countries import countries_list

def categorize_countries(country, condition):
    if condition in country:
        return True
    return False

print(list(filter(lambda country : categorize_countries(country, 'ia'), countries_list)))