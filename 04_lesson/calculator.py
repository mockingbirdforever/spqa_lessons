
class Calculator:

    @staticmethod
    def sum(a, b):
        return a+b

    @staticmethod
    def sub(a, b):
        return a-b

    @staticmethod
    def mul(a, b):
        return a*b

    @staticmethod
    def dev(a, b):
        if b == 0:
            raise ArithmeticError('На ноль делить нельзя')

        return a/b

    @staticmethod
    def pow(a, b=2):
        return a**b

    @staticmethod
    def avg(nums):
        s = 0
        l = len(nums)

        if l == 0:
            return 0

        for num in nums:
            s += num
        return s/l






