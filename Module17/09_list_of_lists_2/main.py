nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

fine_list = [nice_list[i][0] + nice_list[i][1] + nice_list[i][2] for i in range(2)]
perfect_list = fine_list[0] + fine_list[1]
print(perfect_list)