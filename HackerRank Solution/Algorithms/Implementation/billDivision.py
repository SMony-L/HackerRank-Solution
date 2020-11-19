def bonAppetit(bill, k, b):
    # pay = (sum(bill) - bill[k]) / 2
    # if pay == b:
    #     print('Bon Appetit')
    # else:
    #     print(int(sum(bill)/ 2) - pay)
    
    # Compact
    pay = (sum(bill) - bill[k]) / 2
    print('Bon Appetit') if pay == b else print(int(sum(bill)/ 2) - int(pay))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])
    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)