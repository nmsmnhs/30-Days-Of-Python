import re
dic = {}
pattern = r'[^\w\s]'
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
paragraph = re.sub(pattern, ' ', paragraph, re.I)
paragraph = re.split(' ', paragraph)

for word in paragraph:
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] += 1

print(max(dic, key=dic.get))