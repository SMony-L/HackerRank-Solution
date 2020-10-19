from collections import Counter
def migratoryBirds(arr):
    
    # method using Counter
    # print(Counter(arr).most_common(1)[0][0])
    
    # Using sorted function
    print(sorted(list(set(arr)), key=arr.count, reverse=True)[0])

if __name__ == '__main__':
    arr = [1,2,3,4,5,4,3,2,1,3,4]

    result = migratoryBirds(arr)
