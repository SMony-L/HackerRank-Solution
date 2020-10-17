if __name__ == '__main__':
    name = ['Harsh','Anurage']
    score = [[25,26.5,28],[26,28,30]]
    student_marks = dict(zip(name,score))
    queryName = 'Harsh'

    # 1st approach
    # for i in student_marks:
    #     if (i == queryName):
    #         print('{:.2f}'.format(sum(student_marks[i])/3))
    
    # One liner
    print('{:.2f}'.format(sum(list(student_marks[i] for i in student_marks if i == queryName)[0])/3))
