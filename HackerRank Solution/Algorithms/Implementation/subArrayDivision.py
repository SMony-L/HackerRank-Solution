if __name__ == '__main__':
    arr = [1,2,1,3,2]
    d = 3
    m = 2
    counter = 0 
    
    # 1st approach
    for i in range(len(arr)):
        if (sum(arr[i:i+m]) == d):
            counter+= 1
    print(counter)
        

    # oneliner
    # print(sum([1 for i in range(len(arr)) if (sum(arr[i : i + m]) == d)]))