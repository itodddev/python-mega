filenames = ['a.txt', 'b.txt', 'c.txt']

for file in filenames:
    file = open(file, 'r')
    content = file.read()
    print(content)