reply = ['stop', 'quit']
while True:
    user = input('종료하려면 "stop" 또는 "quit" 입력 ?')
    if user not in reply:
        print(user)
        continue
    print(" 종료 ".center(20, '*'))
    break
       
