from countries import countries_list

start = {}

for country in countries_list:
    if country[0] not in start:
        start[country[0]] = 1
    else:
        start[country[0]] += 1

print(start)