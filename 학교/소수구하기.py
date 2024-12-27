num = int(input('값을 입력하세요 : '))
for n in range(2,num):
    for x in range(2, n):
        if n % x == 0:
            print('%d * %d = %d' % (x, n//x, n))
            break
    else:
        print(n, '소수(prime number)')
    

