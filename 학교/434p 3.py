uyear = {1: 'freshman', 2: 'sophomore', 3: 'junior', 4: 'senior'}

try:
    n = int(input('대학교 몇 학년이지요? '))
    if (n > 4):
        raise Exception('예외 발생 이유: 1~4 정수를 입력하세요.')
    
except Exception as e:
    print('예외 발생 이름: {}'.format(type(e)))
    print('예외 발생 이유: 1~4 정수를 입력하세요.'.format(e))
else:
    print('%d학년: %s ' %(n, uyear[n]))
    
finally:
    print('예외 처리가 잘되는군요!')
