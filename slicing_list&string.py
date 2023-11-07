# cara konvensional slicing list & string 

# listmu = [10, 20, 30, 40, 50, 60]
# listku = []
# for i in range(2, 5):
#      listku. append(listmu[i])
# print (f'listku: {listku}')

# cara yang lebih pythonic slicing list & string

listmu = [10, 20, 30, 40, 50, 60]
listku = listmu[2:5]
print (f'listku: {listku}')

kata = 'Anne Sinclair'
print(kata[0:4])