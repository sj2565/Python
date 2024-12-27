F = input('온도 입력 >> ')
C = int(F)
F = C * 9/5 + 32
print('정확 계산: 섭씨:', C, '화씨:', F)
f = C * 2 + 30
print('약식 계산: 섭씨:', C, '화씨:', f)
print('차이:',F-f)
