def plus(a:int,b:int)->int:
    return a+b
def minus(a:int,b:int)->int:
    return a-b
def multiplier(a:int,b:int)->int:
    return a*b
def divisor(a:int,b:int) -> int:
    return a/b


def choose(a:int)->int:
    if a == 1 :
        num1: int
        num2: int
        num1, num2 = map(int,input("두개의 숫자를 입력해주세요: ").split())
        return plus(num1,num2)
    elif a == 2 :
        num1: int
        num2: int
        num1, num2 = map(int,input("두개의 숫자를 입력해주세요: ").split())
        return minus(num1,num2)
    elif a == 3 :
        num1: int
        num2: int
        num1, num2 = map(int,input("두개의 숫자를 입력해주세요: ").split())
        return multiplier(num1,num2)
    elif a == 4 :
        num1: int
        num2: int
        num1, num2 = map(int,input("두개의 숫자를 입력해주세요: ").split())
        return divisor(num1,num2)
    

# 사칙연산 계산기
text = "1.더하기 2.빼기 3.곱하기 4.나누기"
num:int
num = int(input("원하시는 숫자를 눌러주세요: " ))
result = choose(num)
print(f"결과 {result}")




