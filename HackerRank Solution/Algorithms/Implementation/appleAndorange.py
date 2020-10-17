import collections
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # 1st approach
    # appleCounter = 0
    # orangeCounter = 0
    # for i in apples:
    #     if i + a in range(s,t+1):
    #         appleCounter += 1 
    # for i in oranges:
    #     if i + b in range(s,t+1):
    #         orangeCounter += 1 
    # print(appleCounter)
    # print(orangeCounter)
    
    
    # Better solution
    print(sum(collections.Counter([i for i in apples if (i + a) in range (s, t+1)]).values()))
    print(sum(collections.Counter([i for i in oranges if (i + b) in range (s, t+1)]).values()))
    
if __name__ == '__main__':

    s = 7

    t = 11

    a = 5

    b = 15

    m = 3
    n = 2

    apples = [-2,2,1]

    oranges = [5,-6]

    countApplesAndOranges(s, t, a, b, apples, oranges)
