# def plus(a:int,b:int)->int:
#     return a+b
# def minus(a:int,b:int)->int:
#     return a-b
# def multiplier(a:int,b:int)->int:
#     return a*b
# def divisor(a:int,b:int) -> int:
#     return a/b


# def choose(a:int)->int:
#     if a == 1 :
#         num1: int
#         num2: int
#         num1, num2 = map(int,input("두개의 숫자를 입력해주세요: ").split())
#         return plus(num1,num2)
#     elif a == 2 :
#         num1: int
#         num2: int
#         num1, num2 = map(int,input("두개의 숫자를 입력해주세요: ").split())
#         return minus(num1,num2)
#     elif a == 3 :
#         num1: int
#         num2: int
#         num1, num2 = map(int,input("두개의 숫자를 입력해주세요: ").split())
#         return multiplier(num1,num2)
#     elif a == 4 :
#         num1: int
#         num2: int
#         num1, num2 = map(int,input("두개의 숫자를 입력해주세요: ").split())
#         return divisor(num1,num2)
    

# # 사칙연산 계산기
# text = "1.더하기 2.빼기 3.곱하기 4.나누기"
# num:int
# num = int(input("원하시는 숫자를 눌러주세요: " ))
# result = choose(num)
# print(f"결과 {result}")


from calculator import Calculator

clac = Calculator()

num = int(input("1.더하기 2.빼기 3.곱하기 4.나누기"))
text = "원하시는 숫자를 눌러주세요"
num1, num2 = map(int,input("계산한 숫자 두 개를 입력하세요").split())

if num == 1:
    result = clac.add(num1,num2)
elif num == 1:
    result = clac.minus(num1,num2)
elif num == 1:
    result = clac.multiply(num1,num2)
elif num == 1:
    result = clac.divide(num1,num2)
else:
    result = "잘못된 연산 입니다."

print(f"결과{result}")

