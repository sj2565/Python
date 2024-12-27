import pickle as pk

wc = {2010: '남아프리카공화국', 2014: '브라질'}
wc[3] = '2018: 러시아'
win = ['스페인', '독일']
win.append('프랑스')

with open('worldcup.bin', mode='wb') as file:
    pk.dump(wc, file)
    pk.dump(win, file)

with open('worldcup.bin', mode='rb') as file:
    wc = pk.load(file)
    win = pk.load(file)
    print(wc)
    print(win)
