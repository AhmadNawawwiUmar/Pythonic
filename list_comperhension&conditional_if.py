# cara konvensional list comperhension & conditional if 

# listmu = [30, 60, 10, 55]
# listku = []
# for item in listmu:
#      if item > 50:
#          listku. append(item)
# print (f'listmu: {listmu}')
# print (f'listku: {listku}')

# cara yang lebih pythonic list comperhension & conditional if

listmu = [30, 60, 10, 55]
listku = [item for item in listmu if item > 50]
print (f'listmu: {listmu}')
print (f'listku: {listku}')

