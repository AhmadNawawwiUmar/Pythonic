# cara konvensional for loop zip 

# nim = ['001', '002', '603' ]
# nama = ['bejo', 'karti', 'tejo']
# for i, data_nim in enumerate (nama):
#     print(f'{nim[i]} -- {nama[i]}')


# cara yang lebih pythonic for loop zip

nim = ['001', '002', '003' ]
nama = ['bejo', 'karti', 'tejo']
hobby = ['makan', 'menyanyi', 'tidur']

for d_nim, d_nama, d_hobby in zip (nim, nama, hobby):
    print(f'{d_nim} -- {d_nama} -- {d_hobby}')