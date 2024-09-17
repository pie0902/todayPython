class Calculator:
    def add(self, a:int, b:int) -> int:
        return a+b
    def minus(self,a:int, b:int) -> int:
        return a-b
    def multiply(self,a:int,b:int) -> int:
        return a*b
    def divide(self,a:int,b:int)-> float:
        if b == 0:
            return "0을 나눌 수 없습니다."
        return a/b