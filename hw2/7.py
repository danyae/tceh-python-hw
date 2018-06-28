l = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# rows
for i in range(len(l)):
    print(' '.join(str(x) for x in l[i]))

# cols
columns = list(zip(*l))
for i in range(len(columns)):
    print(' '.join(str(x) for x in columns[i]))
