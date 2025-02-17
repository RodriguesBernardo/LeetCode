def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


num = 121

print(isPalindrome(num))