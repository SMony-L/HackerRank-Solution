def breakingRecord(scores):
    minC, maxC = 0,0
    minScore = maxScore = scores[0]

    for i in scores:
        if i > maxScore:
            maxC +=1
            maxScore = i
        if i < minScore:
            minC += 1
            minScore = i

    print(maxC, minC)

if __name__ == '__main__':
    scores = [3,4,21,36,10,28,35,5,24,42]

    result = breakingRecord(scores)


