"""
def ibtido(n):
    
    if n % 4 > 0:
        n = n + (4-n%4)
    
    global a, b, son, list1, list2
    a = int(n/2)
    son = int(a/2+1)
    b = n*1
    list1 = []
    list2 = []

def one(son):
    son -= 2
    betlar1 = [a+2]
    for n in range(son):
        bet = betlar1[n] + 2
        betlar1.append(bet)
    betlar1.reverse()
    return betlar1

def two(son):
    son -= 2
    betlar2 = [1]
    for n in range(son):
        bet = betlar2[n] + 2 
        betlar2.append(bet)
    return betlar2

def three(son):
    son -= 2
    betlar1 = [2]
    for n in range(son):
        bet = betlar1[n] + 2 
        betlar1.append(bet)
    betlar1.reverse()
    return betlar1

def four(son):
    son -= 2
    betlar2 = [a+1]
    for n in range(son):
        bet = betlar2[n] + 2 
        betlar2.append(bet)
    return betlar2

def yakun(n):
    n = int(n)
    ibtido(n)
    bir = one(son)
    ikki = two(son)
    tort = four(son)
    uch = three(son)
    lugat = {}
    lugat['qator1'] = ''
    lugat['qator2'] = ''
    for n in range(son-1):
        list1.append(bir[n]), list1.append(ikki[n]), list2.append(uch[n]), list2.append(tort[n])
    for c in list2:
        
        lugat['qator2'] += f", {c}"
    
    for a in list1:
        lugat['qator1'] += f", {a}"
        
    lugat['listlar'] = int(b/4)
    #lugat['list1'] = list1
    #lugat['list2'] = list2
    return lugat
    #print(int(b/4), 'ta list soling!')
    #print('Birinchi tomon -', list1)
    #print('Ikkinchi tomon -', list2)
"""
