def gradingStudents(grades):
    
    # 1st apprach
    new_grade = []
    for i in grades:
        if (i < 38 or i % 5 < 3):
            new_grade.append(i)
        else:
            # next multiple of 5 is less than 3
            t = (5 - (i % 5)) + i
            new_grade.append(t)
    return new_grade

    # better solution
    # return [x if x < 38 or x % 5 < 3 else (5 - (x % 5)) + x for x in grades]
if __name__ == '__main__':
    grades = [73,67,38,33]
    result = gradingStudents(grades)
    print(result)