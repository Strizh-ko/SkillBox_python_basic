nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]


perfect_list = [x for fine_list in nice_list for each_list in fine_list for x in each_list]
print(perfect_list)