if __name__ == '__main__':
    students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

    # 1st approach
    # secondScore = []
    # for i in students:
    #     secondScore.append(i[1])
    # secondLowest = sorted(set(secondScore))[1]

    # newArr = []
    # for i,j in sorted(students):
    #     if (j == secondLowest):
    #         newArr.append(i)
    # print('\n'.join(sorted(newArr)))
    
    # Better solution
    secondLowest = sorted(set([i[1] for i in students]))[1]
    print('\n'.join(sorted([i for i,j in sorted(students) if j == secondLowest])))