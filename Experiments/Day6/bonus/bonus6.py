contents = ['All carrots are to be sliced longitudinally',
            'The carrots were reportedly sliced',
            'The carrots were cooked']

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

# zip() creates tuples from multiple lists - enumerate() creates an index
# a = [1,2,3]
# b = [10,20,30]
# x = zip(a, b)
# to view contents: list(x)
# [(1,10), (2,20), (3,30)]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)
    file.close()