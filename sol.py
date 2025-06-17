import math

class Solution:
    @staticmethod
    def isPrime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def gcd(numbers):
        result = numbers[0]
        for num in numbers[1:]:
            result = math.gcd(result, num)
        return result

    @staticmethod
    def lcm(numbers):
        result = numbers[0]
        for num in numbers[1:]:
            result = result * num // math.gcd(result, num)
        return result

    @staticmethod
    def solve(n, days):
        days = list(set(days))
        sum = 0
        for i in days:
            if Solution.isPrime(i):
                sum+=i
        if Solution.isPrime(sum):
            return "Both Sided"
        else:
            return "One Sided"
