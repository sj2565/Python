from random import sample
lst = sorted(sample(range(1, 31), 6))
print('원 리스트: ' , (lst)) 
lst1 = list(filter(lambda x: (x%3 == 0), lst))
print('필터 리스트: ' , (lst1))
        
