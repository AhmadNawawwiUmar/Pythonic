# cara konvensional for loop enumerate

# nim = ['001', '002', '003' ]
# nama = ['bejo', 'karti', 'tejo']
# for i in range (len (nim)):
#     print(f'{nim[i]} -- {nama[i]}')

# cara yang lebih pythonic for loop enumerate

nim = ['001', '002', '603' ]
nama = ['bejo', 'karti', 'tejo']
for i, data_nim in enumerate (nim):
     print(f'{nim[i]} -- {nama[i]}')
