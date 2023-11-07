# cara konvensional lambda expression

# def lipat_ganda(x):
#     return x * 2

# listku = [10, 20, 30]
# listmu = list(map(lipat_ganda, listku))
    
# print(f'listku: {listku}')
# print(f'listmu: {listmu}')

# cara yang lebih pythonic lambda expression

listku = [10, 20, 30]
listmu = list(map(lambda x: x * 2, listku))
    
print(f'listku: {listku}')
print(f'listmu: {listmu}')