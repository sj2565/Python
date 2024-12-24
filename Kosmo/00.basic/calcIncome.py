# calcIncome.py
# if 구문 다뤄 보기
# 급여를 입력 받아서, 연봉과 세금 구하기
salary = int(input('급여 입력 : '))
income = 0 # 연본
tax = 0 # 세금

# 연봉이 500 이상이면 12배, 아니면 13배
if salary >= 500 :
    income = 12 * salary
else :
    income = 13 * salary

print(income)

# 세금 : 10000(0.2), 7000(0.15), 5000(0.12), 1000(0.1), else(0)
if income >= 10000 :
    tax = 0.2 * income
elif income >= 7000 :
    tax = 0.15 * income
elif income >= 5000 :
    tax = 0.12 * income
elif income >= 1000 :
    tax = 0.1 * income
else :
    tax = 0

print('급여 : %d' %(salary))
# %.2f는 실수 두번째 자리까지 나타내 줌
print('연봉 : %.2f' %(income))
print('세금 : %.2f' %(tax))