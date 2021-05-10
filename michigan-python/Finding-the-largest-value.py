largest_so_far = -1
print('before', largest_so_far)
for the_num in [9, 41, 15, 13, 3, 74] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('After', largest_so_far)