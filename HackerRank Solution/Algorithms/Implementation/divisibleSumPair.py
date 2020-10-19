from collections import Counter
if __name__ == '__main__':
    arr = [1,3,2,6,1,2]
    k = 3
    counter = 0

    # first attempt
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if((arr[i] + arr[j]) % k == 0):
                counter+=1
    print(counter)

    # oneliner
    # print(sum([1 for i in range(len(arr)) for j in range(i+1, len(arr)) if ((arr[i] + arr[j]) % k == 0)]))
