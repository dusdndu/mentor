# 가중치 << 입력의 중요도
# 편향 << 모델 자체의 기본 성향
# int 개념으로 if문 없이 사용 가능

def step_function(y):
    if y > 0:
        return 1
    else:
        return 0

def AND(x1, x2):
    w1 = 1
    w2 = 1
    b = -1

    y = (w1*x1 + w2*x2) + b

    return int(y > 0)
    
def OR(x1, x2):
    w1 = 1
    w2 = 1
    b = 0

    y = (w1*x1 + w2*x2) + b

    return int(y > 0)
    
def NAND(x1, x2):
    w1 = -1
    w2 = -1
    b = 1

    y = (w1*x1 + w2*x2) + b

    return int(y > 0)

def XOR(x1, x2):
    a = OR(x1, x2)
    b = NAND(x1, x2)
    y = AND(a, b)
    return y