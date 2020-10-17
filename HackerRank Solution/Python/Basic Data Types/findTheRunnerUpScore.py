if __name__ == '__main__':
    n = 5
    arr = [4,2,6,6,5]
    
    # Silly way

    newArr = set(arr)
    newList = list(newArr)
    
    print(newList[-2])

    # Better Solution
    print(list(set(arr))[-2])