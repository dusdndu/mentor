# 가중치 << 입력의 중요도
# 편향 << 모델 자체의 기본 성향



def AND(x1, x2):
    w1 = 1
    w2 = 1
    b = -1

    y = (w1*x1 + w2*x2) + b

    if y >= 1:
        return 1
    else:
        return 0
    
def OR(x1, x2):
    w1 = 1
    w2 = 1
    b = -1

    y = (w1*x1 + w2*x2) + b

    if y >= 0:
        return 1
    else:
        return 0
    
def NAND(x1, x2):
    w1 = -1
    w2 = -1
    b = 2

    y = (w1*x1 + w2*x2) + b

    if y > 0 :
        return 1
    else:
        return 0
    
print(NAND(0, 0))