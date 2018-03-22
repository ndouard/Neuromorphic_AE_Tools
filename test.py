x_indexes = [i for i, j in enumerate(xaddr)] if j == myxaddr]
y_indexes = [i for i, j in enumerate(yaddr)] if j == myyaddr]
print('x_indexes: ' + str(x_indexes))
print('y_indexes:' +str(y_indexes))
# keep common indexes
common = [i for i, j in zip(x_indexes, y_indexes) if i == j]
print('common: ' + str(common))
