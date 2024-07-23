def add(a, b):
     return a+b
    


def subtract(a, b):
	return a-b


def multiply(a, b):
    return a*b


def divide(a, b):
    if b == 0 :
        print("can't divide 0!!!")
        return None
    return a/b


def pow(a, b):
    return a**b


def abs(a):
    if a < 0:
         return -a
    else:
         return a


def mod(a, b):
    if b == 0:
         print('no')
         return -1
    return a%b


if __name__ == "__main__":
    # 간단한 테스트 코드
    pass