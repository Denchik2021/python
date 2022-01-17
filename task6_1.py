res = []
with open ('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        ln = line.split()
        res.append((ln[0], ln[5].strip('"'), ln[6]))
print(res)

result = []

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        element = [line[:line.index('-') - 1]]
        line = line[line.index('"') + 1:]
        element.append(line[:line.index(' ')])
        element.append(line[line.index('/'):line.index('H') -1])
        result.append(tuple(element))

print('[')
for el in result:
    print(el, end=',\n')
print(']')
