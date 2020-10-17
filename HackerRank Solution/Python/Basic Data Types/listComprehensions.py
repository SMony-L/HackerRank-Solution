if __name__ == '__main__':
    x = 1
    y = 1
    z = 2
    n = 3
    # 1st approach
    # newList = []
    # for i in range(x+1):
    #     for j in range(y+1):
    #         for k in range(z+1):
    #             if (i+j+k != n):
    #                 newList.append([i,j,k])
    # print(newList)

    # better solution
    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n])