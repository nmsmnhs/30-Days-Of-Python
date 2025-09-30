countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
three = lambda x : x[0:3]
output = [list(row) for block in countries for row in block]
for row in output:
    row.insert(1, three(row[0]))
    for i in range(3):
        row[i] = row[i].upper()

print(output)