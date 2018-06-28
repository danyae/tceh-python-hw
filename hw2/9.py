l = [1, 2, 3, 4, 5, 'to-delete', 'to-delete', 'to-delete', 'to-delete']
l = [x for x in l if x != 'to-delete']
print(l)
