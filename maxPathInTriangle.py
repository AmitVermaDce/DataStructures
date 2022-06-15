A = [
        [8, 0, 0, 0],
        [4, 4, 0, 0],
        [2, 2, 6, 0],
        [1, 1, 1, 1]
     ]


def tri(A):
    sum = 0
    for sub_list in A:
        max = 0
        for each in sub_list:
            if max < each:
                max = each
        sum += max

    return sum



print(tri(A))
