
#######################################################
col_avg = []                                          #
for j in range(4):                                    #
    column_sum = sum(array[i][j] for i in range(2))   #
    avg = column_sum / 2                              #
    col_avg.append(avg)                               #
#######################################################