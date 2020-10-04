import itertools

row1_gen = (x for x in itertools.permutations([1, 2, 3, 4]))
for row1 in row1_gen:
    # print(row1, 'row1')
    row2_gen = (x for x in itertools.permutations([1, 2, 3, 4]) if
                (x[0] not in [row1[0]]) & (x[1] not in [row1[1]]) & (x[2] not in [row1[2]]) & (x[3] not in [row1[3]]))
    for row2 in row2_gen:
        # print(row2, 'row2')
        row3_gen = (x for x in itertools.permutations([1, 2, 3, 4]) if
                    (x[0] not in [row1[0],row2[0]]) & (x[1] not in [row1[1],row2[1]]) & (x[2] not in [row1[2],row2[2]]) & (x[3] not in [row1[3],row2[3]]))
        for row3 in row3_gen:
            # print(row3, 'row3')
            row4_gen = (x for x in itertools.permutations([1, 2, 3, 4]) if
                        (x[0] not in [row1[0],row2[0],row3[0]]) & (x[1] not in [row1[1],row2[1],row3[1]]) & (x[2] not in [row1[2],row2[2],row3[2]]) & (x[3] not in [row1[3],row2[3],row3[3]]))
            for row4 in row4_gen:
                # print(row4, 'row4')
                cond1 = (row1[0] + row1[1] + row2[0] == 9)
                cond2 = (row1[2] + row1[3] + row2[3] == 4)
                cond3 = (row2[1] + row2[2] + row3[1] + row3[2] == 12)
                cond4 = (row3[0] + row4[0] + row4[1] == 6)
                cond5 = (row3[3] + row4[2] + row4[3] == 9)

                if cond1 & cond2 & cond3 & cond4 & cond5:
                    print('\n', row1, '\n', row2,'\n', row3,'\n', row4)