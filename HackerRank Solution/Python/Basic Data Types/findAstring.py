def countSubString(string,subString):

    # 1st approach
    result = []
    for i in range(len(string)):
        result.append(string[i:i+len(subString)])
    return result.count(subString)
    

    # Better solution
    # return sum(string[i:].startswith(subString) for i in range(len(string)))
if __name__ == '__main__':
    string = "ABCDCDC"
    subString = "CDC"
    count = countSubString(string,subString)
    print(count)
